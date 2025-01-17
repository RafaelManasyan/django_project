from django.urls import path
from django.views.decorators.cache import cache_page

from .views import ProductListView, ProductDetailView, ContactsView, MainView, ProductCreateView, ProductDeleteView, \
    ProductUpdateView, ProductsByCategoryView

app_name = 'catalog'


urlpatterns = [
    path('main/', MainView.as_view(), name='main'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('product_detail/<int:pk>/', cache_page(60*5)(ProductDetailView.as_view()), name='product_detail'),
    path('product_form/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('category/<int:category_id>/', ProductsByCategoryView.as_view(), name='products_by_category'),]
