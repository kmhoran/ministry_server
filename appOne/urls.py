from django.urls import include, path
from appOne import views

urlpatterns = [
    path('', views.index, name='member-index'),
]