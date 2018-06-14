from rest_framework import status, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
# from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
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

class PenguinViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Penguin.objects.all()
    serializer_class = PenguineSerializer