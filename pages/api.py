from django.http import HttpResponseServerError
from django.db.models import Q
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from pages.models import PageDomains, Pages, Profile
from pages.serializers import PageDomainsSerializer, PagesSerializer, ProfileSerializer
from pages.permissions import HasOfficerAccess


class PageDomainsApi(APIView):

    def get(self, request):
        domains = None
        officerAccess = HasOfficerAccess()
        if request.user.is_authenticated and officerAccess.test_request(request):
            domains = PageDomains.objects.all()
        elif request.user.is_authenticated:
            domains = PageDomains.objects.exclude(pages__audience='officers')
        else:
            domains = PageDomains.objects.filter(pages__audience='public')
        serializer = PageDomainsSerializer(domains, many=True)
        if not domains:
            return HttpResponseServerError()
        return Response(serializer.data)
        

class ProfileApi(APIView):
    def get(self, request):
        profile = Profile.objects.filter(user__username=request.user.username)
        if not profile:
            return Response(None)
        serializer = ProfileSerializer
        return Response(serializer.data)


class PageDomainsViewSet(ModelViewSet):
    # permission_classes=[permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = PageDomains.objects.all()
    serializer_class = PageDomainsSerializer

class PagesViewSet(ModelViewSet):
    # permission_classes=[permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Pages.objects.all()
    serializer_class = PagesSerializer
