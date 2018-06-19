from rest_framework import serializers
from pages.models import  PageDomains, Pages, Profile

class PagesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pages
        fields=('id',
                'name',
                'display',
                'url',
                'pageDomain',
                'pageType',
                'audience')

class PageDomainsSerializer(serializers.ModelSerializer):
    pages_set = PagesSerializer(required=False, read_only=True, many=True)
    class Meta:
        model=PageDomains
        fields=('id',
                'name',
                'display', 
                'pages_set') 

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=('firstName',
                'lastName',
                'email',
                'isOfficer')
