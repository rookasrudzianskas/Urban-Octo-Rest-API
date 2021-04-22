from django.db import models


# Create your models here.

class Project(models.Model):

    name = models.CharField(max_length=200)
    language = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    website = models.CharField(max_length=200)

    def __str__(self):
        return self.name
