from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy

from .forms import ProductForm, ProductModeratorForm
from .models import Product
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import ListView, DetailView, TemplateView


class MainView(TemplateView):
    template_name = 'catalog/main.html'


class ProductListView(ListView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm

    def get_form_class(self):
        user = self.request.user
        if user.has_perm('catalog.can_unpublish_product') and user != self.object.owner:
            return ProductModeratorForm
        if user == self.object.owner:
            return ProductForm
        raise PermissionDenied

    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        product = self.get_object()
        if user == product.owner or user.has_perm('catalog.can_delete_product'):
            return super().dispatch(request,*args, **kwargs)
        raise PermissionDenied


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

