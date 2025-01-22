from django import forms
from .models import CommentAnonymous, CommentAuthenticated, Items, Subjects, GalleryItems, Categories


class CommentAnonymousForm(forms.Form):
    name = forms.CharField(label='Имя автора', widget=forms.TextInput(attrs={
        'class': 'form-control custom-form',
        'placeholder': 'Введите имя автора'
    }))
    content = forms.CharField(label='Комментарий', widget=forms.Textarea(attrs={
        'class': 'form-control custom-form',
        'placeholder': 'Введите комментарий',
        'rows': 4,
        'cols': 65
    }))



class CommentAuthenticatedForm(forms.ModelForm):
    class Meta:
        model = CommentAuthenticated
        fields = ['content']
        labels = {
            'content': 'Комментарий',
        }
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control custom-form',
                'placeholder': 'Введите комментарий',
                'rows': 4,
                'cols': 65
            }),
        }



class EditItemForm(forms.ModelForm):
    subject_item = forms.ModelMultipleChoiceField(
        queryset=Subjects.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Тематика товара'
    )

    class Meta:
        model = Items
        fields = [
            'title',
            'price',
            'amount',
            'description',
            'card_description',
            'category',
            'subject_item',
            'slug'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'card_description': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Заголовок',
            'price': 'Цена',
            'amount': 'Количество',
            'description': 'Описание',
            'card_description': 'Короткое описание',
            'category': 'Категория',
            'slug': 'URL-слуг'
        }



class CreateItemForm(forms.ModelForm):
    image = forms.FileField(required=False, label='Изображение товара')
    subject_item = forms.ModelMultipleChoiceField(
        queryset=Subjects.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Тематика товара'
    )

    class Meta:
        model = Items
        fields = [
            'title',
            'price',
            'amount',
            'description',
            'card_description',
            'category',
            'subject_item',
            'slug'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'card_description': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Заголовок',
            'price': 'Цена',
            'amount': 'Количество',
            'description': 'Описание',
            'card_description': 'Короткое описание',
            'category': 'Категория',
            'slug': 'URL-слуг'
        }



class GalleryItemForm(forms.ModelForm):
    class Meta:
        model = GalleryItems
        fields = ['image', 'item']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'item': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'image': 'Изображение товара',
            'item': 'Товар'
        }