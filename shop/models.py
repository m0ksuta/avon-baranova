from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
# User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

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

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.name


class Actual(models.Model):
    name = models.CharField(max_length=250, unique=True, default='')
    image = models.ImageField(upload_to='actual_images', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Актуальное'
        verbose_name_plural = 'Актуальные новости'

    def __str__(self):
        return self.name


class Paragraph(models.Model):
    text = models.TextField()

    class Meta:
        ordering = ('text',)
        verbose_name = 'Текст на главной'
        verbose_name_plural = 'Текст на главной'


class Review(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return 'Comment by {}'.format(self.name)
