from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from main.serializers import MenuSerializer, PageSerializer
from main.models import Menu, Page

# class MenuViewSet(ModelViewSet):
#     queryset = Menu.objects.all()
#     serializer_class = MenuSerializer

# class PageViewSet(ModelViewSet):
#     queryset = Page.objects.all()
#     serializer_class = PageSerializer 