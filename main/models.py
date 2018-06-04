from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=50)
    display = models.CharField(max_length=50)
    def __str__(self):
        return self.display

class Page(models.Model):
    name = models.CharField(max_length=50)
    display = models.CharField(max_length=50)
    url = models.CharField(max_length=150)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
