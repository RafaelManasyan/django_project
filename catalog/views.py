from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .forms import ProductForm
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


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

