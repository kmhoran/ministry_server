from rest_framework.routers import DefaultRouter

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from pages.api import PageDomainsViewSet, PagesViewSet, PageDomainsApi

router = DefaultRouter()
router.register(r'pgd-admin', PageDomainsViewSet)
router.register(r'pg-admin', PagesViewSet)

urlpatterns = router.urls
urlpatterns.append(url(r'^page-domains/$', PageDomainsApi.as_view()))