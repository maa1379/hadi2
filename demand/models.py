from django.contrib.auth import get_user_model
from django.db import models

user = get_user_model()
from product.models import Exportal, Internal


# Create your models here.

class Hold(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11)
    text = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    internal = models.ForeignKey(Internal, on_delete=models.CASCADE, blank=True, null=True)
    exportal = models.ForeignKey(Exportal, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.user} request for holding {self.internal}{self.exportal}'


class ForbiddenWords(models.Model):
    word = models.CharField(max_length=125)

    def __str__(self):
        return self.word


class Visit(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11)
    text = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    internal = models.ForeignKey(Internal, on_delete=models.CASCADE, blank=True, null=True)
    exportal = models.ForeignKey(Exportal, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.user} request for holding {self.internal}{self.exportal}'

class Nemoneh(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11)
    text = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    internal = models.ForeignKey(Internal, on_delete=models.CASCADE, blank=True, null=True)
    exportal = models.ForeignKey(Exportal, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.user} request for holding {self.internal}{self.exportal}'