from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('catalogue/', views.catalogue, name='catalogue'),
    path('<slug:category_slug>', views.catalogue, name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>', views.product, name='product_detail'),
    path('sign_up/', views.sign_up, name='sign_up'),
]
