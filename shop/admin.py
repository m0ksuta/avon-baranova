from django.contrib import admin
from .models import Actual, Category, Paragraph, Product, Review

# Register your models here.
admin.site.register(Product)
admin.site.register(Actual)
admin.site.register(Paragraph)
admin.site.register(Category)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'text')
admin.site.register(Review, CommentAdmin)
