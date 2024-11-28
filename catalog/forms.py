from django import forms
from django.core.exceptions import ValidationError
from catalog.models import Product


BLACK_LIST = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

        for word in BLACK_LIST:
            if word in name:
                self.add_error('name', f'Название не может содержать {word}')
            elif word in description:
                self.add_error('description', f'Описание не может содержать {word}')

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Цена должна быть не отрицательной')
        return price
