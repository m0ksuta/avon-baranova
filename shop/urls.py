from django.urls import include, path

from . import views
from django.conf.urls import url

app_name = 'shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('catalogue/', views.product_list, name='catalogue'),
    path('review/', views.review, name='review'),
    path('account/create/', views.sign_up, name='sign_up'),
    path('account/login/', views.user_login, name='login'),
    path('account/out/', views.sign_out_view, name='sign_out'),
    url(r'^(?P<category_slug>[-\w]+)/$',
        views.product_list,
        name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.product_detail,
        name='product_detail'),
]
