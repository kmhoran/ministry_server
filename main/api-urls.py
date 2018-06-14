from rest_framework.routers import DefaultRouter
from main.api import MenuViewSet, PageViewSet, PenguinViewSet

router = DefaultRouter()
router.register(r'nav-menu', MenuViewSet)
router.register(r'nav-page', PageViewSet)
router.register(r'penguins', PenguinViewSet)

urlpatterns = router.urls