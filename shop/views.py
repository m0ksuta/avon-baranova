from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .forms import LoginForm, SignUpForm
from .models import Actual, Category, Paragraph, Product


def home(request):
    actuals = Actual.objects.all()
    paragraph = Paragraph.objects.all()
    return render(request, 'home.html', {'actuals': actuals, 'paragraph': paragraph})


def cart(request):
    return render(request, 'order.html')


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
            user = authenticate(username=cd['username'], password=cd['password'])
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
    return render(request, 'review.html')
