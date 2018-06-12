from django.contrib import admin
from django.urls import include, path
import oauth2_provider.views as oauth2_views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from appOne.core import views as core_views
# from ministry_server import appOne

# OAuth2 provider endpoints
oauth2_endpoint_views = [
    path('authorize/', oauth2_views.AuthorizationView.as_view(), name="authorize"),
    path('token/', oauth2_views.TokenView.as_view(), name="token"),
    path('revoke-token/', oauth2_views.RevokeTokenView.as_view(), name="revoke-token"),
]



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('api/', include('main.api-urls')),
    path('members/', include('members.urls')),
    path('o/', include(oauth2_endpoint_views, namespace='oauth2_provider')),
    path('', include('public.urls')),   
]
