from django.urls import path
from . import views


app_name = 'catalog'


urlpatterns = [
    path('main/', views.main, name='main'),
    path('contacts/', views.contacts, name='contacts'),
    path('products_list/', views.products_list, name='products_list'),
    path('product/<int:pk>/', views.product, name='product')
]
