from django.urls import path, include

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


    # url(r'^password-reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    # url(r'^password-reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    # url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', 'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    # url(r'^password-reset/complete/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
]
