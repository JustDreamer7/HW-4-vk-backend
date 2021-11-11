from django.db import models


# Create your models here.
class Users(models.Model):
    username = models.EmailField(verbose_name='Имя пользователя', null=False, primary_key=True, default='Ivan@mail.ru')
    company = models.CharField(verbose_name='Компания пользователя', max_length=64, null=True)