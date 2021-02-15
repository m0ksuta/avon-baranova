from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('catalogue/', views.catalogue, name='catalogue'),
    path('<slug:category_slug>', views.catalogue, name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>', views.product, name='product_detail'),
    path('account/create/', views.sign_up, name='sign_up'),
    path('account/login/', views.user_login, name='login'),
    path('account/out/', views.sign_out_view, name='sign_out'),
    path('order/', views.cart, name='cart'),
    path('review/', views.review, name='review'),
]
