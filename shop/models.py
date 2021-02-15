from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

# User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product', blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='')

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.name


class Actual(models.Model):
    name = models.CharField(max_length=250, unique=True, default='')
    image = models.ImageField(upload_to='actual_images', blank=True)

    def __str__(self):
        return self.name


class Paragraph(models.Model):
    text = models.TextField()

# def get_sentinel_user():
#     return get_user_model().objects.get_or_create(username='deleted')[0]


'''class UserModelForm(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    birth_date = models.DateField(default='')
    living_address = models.CharField(max_length=500)
    living_index = models.IntegerField()
    registration_address = models.CharField(max_length=500)
    registration_index = models.IntegerField()
    passport_organization = models.CharField(max_length=500)
    passport_date = models.DateField(default='')
    passport_series = models.IntegerField()
    passport_number = models.IntegerField()

    def __str__(self):
        return self.username
'''
