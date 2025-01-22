from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login_page'),
    path('register/', views.register_view, name='register_page'),
    path('logout/', views.logout_active, name='logout_active'),
    path('show/profile', views.show_profile_view, name='profile_page'),
    path('edit/profile',views.EditProfile.as_view(), name='edit_profile_active')
]
