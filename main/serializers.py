from rest_framework import serializers
from main.models import Menu, Page, Penguin

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Page
        fields=('id',
                'name',
                'display',
                'url',
                'menu')

class MenuSerializer(serializers.ModelSerializer):
    page_set = PageSerializer(required=False, read_only=True, many=True)
    class Meta:
        model=Menu
        fields=('id',
                'name',
                'display', 
                'audience',
                'page_set') 

class PenguineSerializer(serializers.ModelSerializer):
    class Meta:
        model=Penguin
        fields=('id',
                'name',
                'color',
                'is_black')