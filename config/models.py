from django.db import models


# Create your models here.
class EmailSave(models.Model):
    subject = models.CharField(max_length=350)
    message = models.TextField()
    created=models.DateField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.subject

class IPAddress(models.Model):
	ip_address = models.GenericIPAddressField(verbose_name="آدرس آی‌پی")