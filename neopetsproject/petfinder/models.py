from django.db import models

# Create your models here.
class Pet(models.Model):
    id = models.IntegerField(primary_key=True)
    animal_type = models.CharField(max_length=50)
    detail_link = models.CharField(max_length=300)
    age = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    zipcode = models.IntegerField()