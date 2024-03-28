from django.db import models

# Create your models here.'
class allpets(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='pimages',null = True, blank = True)

class contactus(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    msg=models.TextField()


