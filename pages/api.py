from django.http import HttpResponseServerError
from django.db.models import Q
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from pages.models import PageDomains, Pages
from pages.serializers import PageDomainsSerializer, PagesSerializer
from pages.permissions import HasOfficerAccess


class PageDomainsApi(APIView):

    def get(self, request):
        domains = None
        if request.user.is_authenticated and HasOfficerAccess.has_permission(request, self):
            domains = PageDomains.objects.all()
        elif request.user.is_authenticated:
            domains = PageDomains.objects.filter(audience!='officers')
        else:
            domains = PageDomains.objects.filter(audience='public')
        serializer = PageDomainsSerializer(domains, many=True)
        if not domains:
            return HttpResponseServerError()
        return Response(serializer.data)
        


class PageDomainsViewSet(ModelViewSet):
    # permission_classes=[permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = PageDomains.objects.all()
    serializer_class = PageDomainsSerializer

class PagesViewSet(ModelViewSet):
    # permission_classes=[permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Pages.objects.all()
    serializer_class = PagesSerializer
