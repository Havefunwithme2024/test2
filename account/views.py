from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.views.generic import UpdateView
from django.urls import reverse_lazy

from .forms import LoginForm, RegistrationForm, EditProfileForm
from .models import Profile
from pages.models import CommentAuthenticated, FavoriteItems, Items


def login_view(request):
    if request.method == 'POST':
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('index_page')
    else:
        login_form = LoginForm()

    context = {
        'login_form': login_form
    }
    return render(request, 'account/login.html', context)


def register_view(request):
    if request.method == 'POST':
        register_form = RegistrationForm(data=request.POST)
        if register_form.is_valid():
            user = register_form.save()
            profile = Profile.objects.create(user=user)
            profile.save()
            return redirect('login_page')
    else:
        register_form = RegistrationForm()

    context = {
        'register_form': register_form
    }
    return render(request, 'account/register.html', context)


def logout_active(request):
    logout(request)
    return redirect('index_page')

def show_profile_view(request):
    if request.user.is_authenticated:
        user =request.user
        profile = Profile.objects.get(user=user)
        favorite_count = FavoriteItems.objects.filter(author=user).count()
        comment_count = CommentAuthenticated.objects.filter(user=user).count()
        item_count = Items.objects.filter(author=user).count()
        context = {
            'profile': profile,
            'title': 'Мой профиль',
            'favorite_count':favorite_count,
            'comment_count': comment_count,
            'item_count': item_count
        }
        return render(request, 'account/profile.html', context)

class EditProfile(UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = 'account/edit_profile.html'
    extra_context = {
        'title': 'Изменения профиля'
    }

    def get_success_url(self):
        return reverse_lazy('profile_page')

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, user=self.request.user)




