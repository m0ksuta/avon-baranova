from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])

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


class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']
        db_table = 'Cart'

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'CartItem'

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product


class Order(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    date_range = 100
    birth_date = models.DateField()
    living_address = models.CharField(max_length=500)
    living_index = models.CharField(max_length=6)
    registration_address = models.CharField(max_length=500)
    registration_index = models.CharField(max_length=6)
    passport_organization = models.CharField(max_length=500)
    passport_date = models.DateField()
    passport_series = models.CharField(max_length=4)
    passport_number = models.CharField(max_length=6)

"""
---
"""


