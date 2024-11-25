from django.urls import path
from .views import ProductListView, ProductDetailView, ContactsView, MainView

app_name = 'catalog'


urlpatterns = [
    path('main/', MainView.as_view(), name='main'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('products_list/', ProductListView.as_view(), name='products_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='products')
]
