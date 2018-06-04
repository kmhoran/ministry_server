from django.shortcuts import render
from main.serializers import MenuSerializer
from main.models import Menu, Page
# Create your views here.

def index(request):
    queryset = Menu.objects.all()
    serializer = MenuSerializer(queryset)
    return render(
        request,
        'appOne/index.html',
        context={'nav':serializer.data},
    )
