from django.urls import reverse_lazy

from blog.models import Article
from django.views.generic import ListView, TemplateView, DetailView, UpdateView, CreateView, DeleteView


class ArticleTemplateView(TemplateView):
    template_name = 'blog/base.html'


class ArticleListView(ListView):
    model = Article


class ArticleDetailView(DetailView):
    model = Article

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class ArticleCreateView(CreateView):
    model = Article
    fields = ('title', 'content', 'preview_img',)
    success_url = reverse_lazy('blog:article_list')


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'content', 'preview_img',)

    def get_success_url(self):
        return reverse_lazy('blog:article_detail', kwargs={'pk': self.object.pk})


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('blog:article_list')
