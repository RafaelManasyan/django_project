from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Изображение')
    category = models.CharField(max_length=150, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена за покупку')
    created_at = models.DateField(verbose_name='Дата создания продукта')
    updated_at = models.DateField(verbose_name='Дата последних изменений')

    def __str__(self):
        return f'''Наименование - {self.name}. Цена - {self.price}.'''

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'Категория - {self.name}. Описание: {self.description}.'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
