from django.urls import path
from blog.views import ArticleTemplateView, ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

app_name = 'blog'


urlpatterns = [
    path('base/', ArticleTemplateView.as_view(), name='base'),
    path('article_list/', ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/article_detail/', ArticleDetailView.as_view(), name='article_detail'),
    path('article_form/', ArticleCreateView.as_view(), name='article_form'),
    path('<int:pk>/update/', ArticleUpdateView.as_view(), name='article_update'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
]
