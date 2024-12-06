from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email

    avtr = models.ImageField(verbose_name='Аватар', blank=True)
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=15)
    country = models.CharField(verbose_name='Страна', max_length=100)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_perms',
        blank=True,
    )

