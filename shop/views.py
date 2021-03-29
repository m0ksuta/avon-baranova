from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .forms import LoginForm, OrderForm, ReviewForm, SignUpForm
from .models import (Actual, Cart, CartItem, Category, Order, Paragraph,
                     Product, Review)


def home(request):
    actuals = Actual.objects.all()
    paragraph = Paragraph.objects.all()
    return render(request, 'shop/home.html', {'actuals': actuals,
                                              'paragraph': paragraph})


def product_list(request, category_slug=None):
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
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request,
                  'shop/product/detail.html',
                  {'product': product})


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            signup_user = User.objects.get(username=username)
        else:
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user =  authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('catalogue')
                else:
                    return HttpResponse('Disabled account')
            else:
                return redirect('login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def sign_out_view(request):
    logout(request)
    return redirect('login')


def review(request):
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


def password_reset(request):
    form = PasswordResetForm()
    return render(request, 'password_reset.html', {'form': form})
