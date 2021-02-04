from django.contrib import admin

from .models import Actual, Paragraph, Product

# Register your models here.
admin.site.register(Product)
admin.site.register(Actual)
admin.site.register(Paragraph)
