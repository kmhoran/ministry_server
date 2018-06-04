from django.shortcuts import render
from main.serializers import MenuSerializer
from main.models import Menu, Page
# Create your views here.

def index(request):
    nav = None
    if request.user.is_authenticated:
        queryset = Menu.objects.all()
        serializer = MenuSerializer(queryset, many=True)
        nav = serializer.data
    return render(
        request,
        'main/index.html',
        context={'nav':nav},
    )
