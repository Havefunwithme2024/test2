from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250, null=True, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=250, null=True, blank=True, verbose_name='Фамилия')
    age = models.IntegerField(default=0, verbose_name='Возраст')