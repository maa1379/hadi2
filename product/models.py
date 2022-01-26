from django.contrib.auth import get_user_model
from django.db import models

user = get_user_model()


# Create your models here.
class Exportal(models.Model):
    mine = models.CharField(max_length=255)
    kode_sine_kar = models.CharField(max_length=255)
    kode_peleh = models.CharField(max_length=255)
    stone_name = models.CharField(max_length=255)
    created = models.DateField()
    shomareh_serail_qoleh_dr_madan = models.CharField(max_length=255)
    kode_darz = models.CharField(max_length=255)
    kode_ghavareh = models.CharField(max_length=255)
    kode_rang = models.CharField(max_length=255)
    length = models.PositiveIntegerField()
    width = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
    vazne_taghribi = models.PositiveIntegerField()
    vazne_baskol = models.PositiveIntegerField()
    buyer = models.CharField(max_length=255)
    uniqu_id = models.CharField(max_length=255, blank=True, null=True)
    uploder = models.ForeignKey(user, on_delete=models.SET_NULL, null=True, blank=True)
    image1 = models.ImageField(upload_to="images/", null=True, blank=True)
    image2 = models.ImageField(upload_to="images/", null=True, blank=True)
    image3 = models.ImageField(upload_to="images/", null=True, blank=True)
    image4 = models.ImageField(upload_to="images/", null=True, blank=True)

    def save(self, *args, **kwargs):
        color = self.kode_rang
        year = str(self.created)
        month = str(self.created)
        goleh = self.shomareh_serail_qoleh_dr_madan
        darz = self.kode_darz
        ghavareh = self.kode_ghavareh
        self.uniqu_id = color + '-' + year[3] + month[5] + month[6] + goleh + '-' + darz + ghavareh
        super(Exportal, self).save(*args, **kwargs)


class Internal(models.Model):
    mine = models.CharField(max_length=255)
    kode_sine_kar = models.CharField(max_length=255)
    shomareh_serail_qoleh_dr_madan = models.CharField(max_length=255)
    stone_name = models.CharField(max_length=255)
    created = models.DateField()
    kode_darage_bandi = models.CharField(max_length=255)
    tonazh_taghribi = models.PositiveIntegerField()
    uniqu_id = models.CharField(max_length=255, blank=True, null=True)
    uploder = models.ForeignKey(user, on_delete=models.SET_NULL, null=True, blank=True)
    image1 = models.ImageField(upload_to="images/", null=True, blank=True)
    image2 = models.ImageField(upload_to="images/", null=True, blank=True)
    image3 = models.ImageField(upload_to="images/", null=True, blank=True)
    image4 = models.ImageField(upload_to="images/", null=True, blank=True)
    line = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        kode_sine_kar = self.kode_sine_kar
        kode_darage_bandi = self.kode_darage_bandi
        shomareh_ghole = self.shomareh_serail_qoleh_dr_madan
        year = str(self.created)[3]
        month = str(self.created)[5:7]
        day = str(self.created)[8::]
        mine = self.mine
        uniqu_id = models.CharField(max_length=255, blank=True, null=True)
        self.uniqu_id = kode_sine_kar + kode_darage_bandi + '-' + shomareh_ghole + year + month + day + '-' + mine
        super(Internal, self).save(*args, **kwargs)


class UpdateInfo(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE,related_name="uplode")
    file_name = models.CharField(max_length=125)
    created = models.DateField(auto_now_add=True)
