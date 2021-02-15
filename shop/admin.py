from django.contrib import admin

from .models import Actual, Category, Paragraph, Product

# Register your models here.
admin.site.register(Product)
admin.site.register(Actual)
admin.site.register(Paragraph)
admin.site.register(Category)
# admin.site.register(UserModelForm)
