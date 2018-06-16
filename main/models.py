from django.db import models

class Menu(models.Model):

    class Meta:
        permissions = (
            ("can_access_member_menu", "ministry members with member site access"),
            ("can_access_officer_menu", "ministry officers with officer site access"),
        )

    name = models.CharField(max_length=50)
    display = models.CharField(max_length=50)
    audience = models.CharField(max_length=50)
    def __str__(self):
        return self.display

class Page(models.Model):
    name = models.CharField(max_length=50)
    display = models.CharField(max_length=50)
    url = models.CharField(max_length=150)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)


class Penguin(models.Model):
    
    class Meta:
        permissions = (
            ("can_see_penguins","Ability to see penguins"),
        )

    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    @property
    def is_black(self):
        return True if self.color == 'black' else False
