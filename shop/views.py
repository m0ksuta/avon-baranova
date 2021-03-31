from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .forms import ReviewForm
from .models import (Actual, Category, Paragraph,
                     Product, Review)


def home(request):
    """
    Функция домашней страницы
    url имеет вид: protocol://domain_name:port
    """
    actuals = Actual.objects.all()
    paragraph = Paragraph.objects.all()
    return render(request, 'shop/home.html', {'actuals': actuals,
                                              'paragraph': paragraph})


def product_list(request, category_slug=None):
    """
    Функция каталога
    Принимает параметр category_slug,
    Он регулирует отображение качества продуктов на странице
    url имеет вид: protocol://domain_name:port/catalogue/
    """
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    """
    Функция отображения конкретного товара
    Принимает параметры id и slug
    id привязан к определенному товару из бд
    slug аналогично, он устанавливает буквенное значение
    и сравнивает его с id
    url имеет вид: protocol://domain_name:port/(переменное значение<id><slug>)
    """
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request,
                  'shop/product/detail.html',
                  {'product': product})


def review(request):
    """
    Функция создания отзывов
    Берет форму ReviewForm из .forms
    Передает в неё параметры, вводимые пользователем
    в поля данной формы
    В слуае, если отзыв проходит валидацию,
    то на странице появляется новый отзыв,
    и пользователь переходит в начало страницы
    url имеет вид: protocol://domain_name:port/review/
    """
    comments = Review.objects.all().filter(active=True)
    if request.method == 'POST':
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.save()
            return HttpResponseRedirect(request.path)
    else:
        form = ReviewForm()
    return render(request, 'shop/review.html', {'form': form,
                                           'comments': comments})
