from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from appOne.core import views as core_views
# from ministry_server import appOne

from appOne.views import ApiEndpoint


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('api/', include('main.api-urls')),
    path('members/', include('members.urls')),
    # path('o/', include('appOne.oauth_urls')),
    path('o/', include('appOne.oauth_urls', namespace="oauth2_provider")),
    path('api/hello', ApiEndpoint.as_view()),
    path('', include('public.urls')),   
]
