from django.urls import include, path
from public import views

urlpatterns = [
    path('', views.index, name='public-index'),
]