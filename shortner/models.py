from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Url(models.Model):
    link = models.CharField(max_length=100000)
    uuid = models.CharField(max_length=10)
    