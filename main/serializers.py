from rest_framework import serializers
from main.models import Menu, Page

# class PageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Page
#         fields=('id',
#                 'name',
#                 'display',
#                 'url',
#                 'menu')

# class MenuSerializer(serializers.ModelSerializer):
#     page_set = PageSerializer(required=False, read_only=True, many=True)
#     class Meta:
#         model=Menu
#         fields=('id',
#                 'name',
#                 'display',
#                 'page_set') 