from django.shortcuts import get_object_or_404, render

from .models import Actual, Paragraph, Product, Category

# Create your views here.


def home(request):
    actuals = Actual.objects.all()
    paragraph = Paragraph.objects.all()
    return render(request, 'home.html', {'actuals': actuals, 'paragraph': paragraph})


def catalogue(request, category_slug=None):
    category_page = None
    products = None
    if category_slug is not None:
        category_page = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category_page, available=True)
    else:
        products = Product.objects.all().filter(available=True)
    return render(request, 'catalogue.html', {'products': products, 'category': category_page})


def product(request, category_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'product.html', {'product': product})
