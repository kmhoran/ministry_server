from django.db import models
from django.contrib.auth.models import User

class PageDomains(models.Model):

    class Meta:
        permissions = (
            ("has_officer_access", "members with officer site access"),
        )

    name = models.CharField(max_length=50)
    display = models.CharField(max_length=50)
    def __str__(self):
        return self.display

class Pages(models.Model):
    name = models.CharField(max_length=50)
    display = models.CharField(max_length=50)
    url = models.CharField(max_length=150)
    pageDomain = models.ForeignKey('PageDomains', on_delete=models.CASCADE)
    pageType = models.CharField(max_length=50)
    audience = models.CharField(max_length=50)

    def __str__(self):
        return self.display

class Profile(models.Model):
    user =  models.OneToOneField(User, on_delete=models.CASCADE)
    @property
    def isOfficer(self):
        return self.user.groups.filter(name="MinistryOfficer").exists()
    
    @property
    def email(self):
        return self.user.email
    
    @property
    def firstName(self):
        return self.user.first_name

    @property
    def lastName(self):
        return self.user.last_name
        

