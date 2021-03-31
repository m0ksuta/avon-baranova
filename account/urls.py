from django.urls import include, path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth import login, logout
from . import views


app_name = 'account'

urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^logout-then-login/$', auth_views.logout_then_login,
        name='logout_then_login'),
]
