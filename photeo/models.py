from django.db import models

# Create your models here.
class Contestant(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128, default='')
    picture = models.ImageField(upload_to='images/', null=True)
    title = models.CharField(max_length=512)
    social_account = models.CharField(max_length=512, blank=True)
    votes = models.IntegerField(default=0)

class Voter(models.Model):
    email = models.CharField(max_length=256)
    vote = models.ForeignKey(Contestant, on_delete=models.CASCADE)
    verified = models.BooleanField(default=False)