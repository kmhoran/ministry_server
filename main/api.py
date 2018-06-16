from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.mixins import PermissionRequiredMixin
from rest_framework.viewsets import ModelViewSet
# from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from main.permissions import CanSeePenguins,CanViewMemberMenu, CanViewOfficerMenu
from main.serializers import MenuSerializer, PageSerializer, PenguineSerializer
from main.models import Menu, Page, Penguin

class MenuViewSet(ModelViewSet):
    # permission_classes=[permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class PageViewSet(ModelViewSet):
    # permission_classes=[permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Page.objects.all()
    serializer_class = PageSerializer 

class PenguinViewSet(ModelViewSet, PermissionRequiredMixin):
    # permission_required = 'catalog.can_see_penguins'
    permission_classes = (permissions.IsAuthenticated, CanSeePenguins,)
    queryset = Penguin.objects.all()
    serializer_class = PenguineSerializer


class PublicMenuSet(ModelViewSet):
    queryset = Menu.objects.filter(audience="public")
    serializer_class = MenuSerializer


class MemberMenuSet(ModelViewSet):
    permission_classes=(permissions.IsAuthenticated, CanViewMemberMenu,)
    queryset = Menu.objects.filter(audience="members")
    serializer_class = MenuSerializer


class OfficerMenuSet(ModelViewSet):
    permission_classes=(permissions.IsAuthenticated, CanViewOfficerMenu,)
    queryset = Menu.objects.filter(audience="officers")
    serializer_class = MenuSerializer