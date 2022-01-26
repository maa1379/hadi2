from django.db import models


# Create your models here.
class Madan(models.Model):
    name = models.CharField(max_length=125)
    stone_type = models.CharField(max_length=125)
    shomareh_mojavez_kashf = models.CharField(max_length=25,null=True,blank=True)
    shomareh_parvaneh_bahrevardari = models.CharField(max_length=25,null=True,blank=True)
    tonazh_bahrebardari = models.CharField(max_length=25,null=True,blank=True)
    payment = models.CharField(max_length=125)
    province = models.CharField(max_length=125)
    city = models.CharField(max_length=125)
    village = models.CharField(max_length=125)
    location_url = models.URLField(null=True,blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name
