from django.urls import include, path
from members import views

urlpatterns = [
    path('', views.index, name='members-index'),
]