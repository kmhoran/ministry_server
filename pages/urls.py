from rest_framework.routers import DefaultRouter
from pages.api import PageDomainsViewSet
# , PageDomainsApi

router = DefaultRouter()
# router.register(r'page-domains', PageDomainsApi)
router.register(r'pg-admin', PageDomainsViewSet)

urlpatterns = router.urls