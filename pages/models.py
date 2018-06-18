from django.db import models

class PageDomains(models.Model):

    class Meta:
        permissions = (
            ("has_officer_access", "members with officer site access"),
        )

    name = models.CharField(max_length=50)
    display = models.CharField(max_length=50)
    audience = models.CharField(max_length=50)
    def __str__(self):
        return self.display

class Pages(models.Model):
    name = models.CharField(max_length=50)
    display = models.CharField(max_length=50)
    url = models.CharField(max_length=150)
    pageDomain = models.ForeignKey('PageDomains', on_delete=models.CASCADE)
    content = models.CharField(max_length=10000)
    pageType = models.CharField(max_length=50)

    def __str__(self):
        return self.display

    