from rest_framework import serializers
from pages.models import  PageDomains, Pages

class PagesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pages
        fields=('id',
                'name',
                'display',
                'url',
                'pageDomain',
                'content',
                'pageType')

class PageDomainsSerializer(serializers.ModelSerializer):
    pages_set = PagesSerializer(required=False, read_only=True, many=True)
    class Meta:
        model=PageDomains
        fields=('id',
                'name',
                'display', 
                'audience',
                'pages_set') 
