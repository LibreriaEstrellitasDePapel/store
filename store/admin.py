from django.contrib import admin
from .models import Book, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'stock', 'category')
    list_filter = ('category',)
    search_fields = ('title',)
