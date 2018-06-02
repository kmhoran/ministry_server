from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from appOne.core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, {'next_page':'/outside'}, name='logout'),
    path('register/', core_views.register, name='register'),
    path('users/', TemplateView.as_view(template_name='appOne/users.html')),
    path('outside/', TemplateView.as_view(template_name='appOne/outside.html')),
    path('', TemplateView.as_view(template_name="appOne/index.html"))
]
