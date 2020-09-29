from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'slug', 'author', 'publicado', 'status', 'imagem')
    list_filter = ('status', 'criado', 'publicado', 'author')
    date_hierarchy = 'publicado'
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug':('title',)}