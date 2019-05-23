from django.db import models

class Pet(models.Model):
    animal_id = models.IntegerField(primary_key=True)
    animal_type = models.CharField(max_length=50)
    detail_link = models.CharField(max_length=300)
    image = models.CharField(max_length=300, default='http://placekitten.com/100/150')
    age = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    size = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=500, null=True)
    status = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=50)
    zipcode = models.IntegerField()

