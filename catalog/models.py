from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Изображение', blank=True)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True, blank=True, related_name='category')
    price = models.IntegerField(verbose_name='Цена за покупку')
    created_at = models.DateField(verbose_name='Дата создания продукта')
    updated_at = models.DateField(verbose_name='Дата последних изменений')
    is_published = models.BooleanField(verbose_name='Опубликовать', default='False')
    owner = models.ForeignKey(User, verbose_name='Владелец', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'''Наименование - {self.name}. Цена - {self.price}.'''

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        permissions = [
            ('can_unpublish_product', 'Can unpublish product'),
        ]
