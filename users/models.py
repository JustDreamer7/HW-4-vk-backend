from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    username = models.CharField(verbose_name='Имя пользователя', max_length=50, blank=True, unique=True)
    email = models.EmailField(verbose_name='Почта пользователя', null=False, blank=True, unique=True)
    company = models.CharField(verbose_name='Компания пользователя', max_length=64, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'company']

    def __str__(self):
        return "{}".format(self.email)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
