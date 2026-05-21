from django.contrib import admin
from blog.models import Tag, Category, Page, Post

# Register your models here.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'slug',
    list_display_links = 'name', 
    search_fields = 'id', 'name', 'slug',
    list_per_page = 10
    ordering = '-id', 
    list_display = 'id', 'name', 'slug',
    prepopulated_fields = {
        'slug': ('name',),
    }

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'slug',
    list_display_links = 'name', 
    search_fields = 'id', 'name', 'slug',
    list_per_page = 10
    ordering = '-id', 
    list_display = 'id', 'name', 'slug',
    prepopulated_fields = {
        'slug': ('name',),
    }

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'slug', 'is_published',
    list_display_links = 'title', 
    search_fields = 'id', 'title', 'slug',
    list_editable = 'is_published',
    list_per_page = 10
    ordering = '-id', 
    prepopulated_fields = {
        'slug': ('title',),
    }

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'slug', 'is_published', 'created_at', 'updated_at', 'category', 
    list_display_links = 'title', 
    search_fields = 'id', 'title', 'slug', 'title', 'excerpt', 'content', 
    list_editable = 'is_published',
    list_per_page = 50
    list_filter = 'category', 'is_published',
    ordering = '-id', 
    prepopulated_fields = {
         'slug': ('title',),
    }
    autocomplete_fields = 'tags', 'category',
