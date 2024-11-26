from django.urls import path
from .views import ProductListView, ProductDetailView, ContactsView, MainView, ProductCreateView, ProductDeleteView, \
    ProductUpdateView

app_name = 'catalog'


urlpatterns = [
    path('main/', MainView.as_view(), name='main'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product_form/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]
