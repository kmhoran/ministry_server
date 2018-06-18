from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from pages.models import PageDomains, Pages
from pages.serializers import PageDomainsSerializer, PagesSerializer


# class PageDomainsApi(APIView):
#     serializer_class = PageDomainsSerializer

#     def get(self, request):
#         if not request.user.is_authenticated:
#             print("not authenticated")
#             queryset = PageDomains.objects.filter(audience='public')
#             serializer = PageDomainsSerializer(queryset, many=True)
#             return Response(serializer.data)
#         else:
#             print("authenticated")
#             queryset = PageDomains.objects.all()
#             serializer = PageDomainsSerializer(queryset, many=True)
#             return Response(serializer.data)


class PageDomainsViewSet(ModelViewSet):
    # permission_classes=[permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = PageDomains.objects.all()
    serializer_class = PageDomainsSerializer

class PagesViewSet(ModelViewSet):
    # permission_classes=[permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Pages.objects.all()
    serializer_class = PagesSerializer
