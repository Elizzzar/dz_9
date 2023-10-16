from django.db import models

# Create your models here.

class Test_model(models.Model):
    name = models.CharField(max_length=200)
    array_json = models.JSONField()