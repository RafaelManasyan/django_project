from django.contrib import admin
from blog.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_filter = ('is_active',)
    list_display = ('id', 'title', 'created_at',)
    search_fields = ('title',)
