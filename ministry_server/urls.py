
from django.urls import include, path
from django.views.generic import TemplateView
from django.contrib import admin
from django.contrib.auth.models import User, Group
admin.autodiscover()



# from appOne.core import views as core_views
# from ministry_server import appOne

# from appOne.views import ApiEndpoint


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/', include('main.api-urls')),
    path('members/', include('members.urls')),
    # path('o/', include('appOne.oauth_urls')),
    # path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('', include('public.urls')),   
]
