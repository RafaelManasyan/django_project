from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        category, _ = Category.objects.get_or_create(name='Сыпучка', description='Инертные материалы на продажу')

        products = [
            {"name": "Чернозем",
             "description": "Темная плодородная и рыхлая земля",
             "image": "",
             "category": category,
             "price": 500,
             "created_at": "2024-10-10",
             "updated_at": "2024-11-11"},
            {"name": "Samsung S22 Ultra",
             "description": "Лучший андроид смартфон в мире",
             "image": "",
             "category": category,
             "price": 100001,
             "created_at": "2024-05-05",
             "updated_at": "2024-09-09"}
        ]

        for prod in products:
            product, created = Product.objects.get_or_create(**prod)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Успешно зарегистрирован товар: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Товар уже зарегистрирован: {product.name}'))

