from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from appOne.core import views as core_views
import appOne
# from ministry_server import appOne

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    
    path('members/', include('appOne.urls')),
    path('', TemplateView.as_view(template_name='main/index.html'), name='index'),   
]
