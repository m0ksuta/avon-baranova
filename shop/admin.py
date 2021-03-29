from django.contrib import admin
from .models import Actual, Category, Paragraph, Product, Review


# Register your models here.
admin.site.register(Actual)
admin.site.register(Paragraph)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'text')
admin.site.register(Review, CommentAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)
