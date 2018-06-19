from rest_framework.routers import DefaultRouter
from main.api import MenuViewSet, PageViewSet, PenguinViewSet, PublicMenuSet, MemberMenuSet, OfficerMenuSet

router = DefaultRouter()
# router.register(r'nav-menu', MenuViewSet)
# router.register(r'public-menus', PublicMenuSet)
# router.register(r'member-menus', MemberMenuSet)
# router.register(r'officer-menus', OfficerMenuSet)
# router.register(r'nav-page', PageViewSet)
router.register(r'penguins', PenguinViewSet)

urlpatterns = router.urls