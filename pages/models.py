from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator, MinLengthValidator


class Categories(models.Model):
    name = models.CharField(max_length=250, verbose_name='Имя категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Subjects(models.Model):
    name = models.CharField(max_length=250, verbose_name='Имя тематики')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тематика'
        verbose_name_plural = 'Тематики'

class Items(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название Товара')
    price = models.IntegerField(verbose_name='Цена товара')
    quantity_views = models.IntegerField(default=0, verbose_name='Кол-во просмотров товара')
    description = models.TextField(verbose_name='Описание')
    card_description = models.TextField(verbose_name='Короткое описание', validators=[

        MinLengthValidator(25),

        MaxLengthValidator(35)
    ])
    is_available = models.BooleanField(default=True, verbose_name='Доступность')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name='Категория')
    creation_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Время и дата создания')
    updates_datetime = models.DateTimeField(auto_now=True, verbose_name='Время и дата обновления')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Продавец')
    subject_item = models.ManyToManyField(Subjects, verbose_name='Тематика товара')
    amount = models.IntegerField(default=1, verbose_name='Доступность')
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return self.title

    def get_first_photo(self):
        try:
            photo = self.gallery_articles.all().first()
            return photo.image.url
        except Exception as e:
            print(e)
            return 'https://cdn.vectorstock.com/i/500p/46/50/missing-picture-page-for-website-design-or-mobile-vector-27814650.jpg'

    def get_all_photo(self):
        try:
            photo = self.gallery_articles.all()[1:]
            return photo
        except Exception as e:
            print(e)
            return 'https://cdn.vectorstock.com/i/500p/46/50/missing-picture-page-for-website-design-or-mobile-vector-27814650.jpg'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class GalleryItems(models.Model):
    image = models.ImageField(upload_to='articles/', verbose_name='Фотки')
    item = models.ForeignKey(Items, on_delete=models.CASCADE, related_name='gallery_item')


class CommentAnonymous(models.Model):
    name = models.CharField(max_length=250, verbose_name='Автор комментария')
    content = models.TextField(verbose_name='Описание комментария')
    datetime_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    item = models.ForeignKey(Items, on_delete=models.CASCADE)

class CommentAuthenticated(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор комментария')
    content = models.TextField(verbose_name='Описание комментария')
    creation_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    item = models.ForeignKey(Items, on_delete=models.CASCADE, verbose_name='Товар')

class ViewsItems(models.Model):
    item = models.ForeignKey(Items, on_delete =models.CASCADE)
    user_session = models.CharField(max_length=250)

class FavoriteItems(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)