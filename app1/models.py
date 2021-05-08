from django.db import models
# Create your models here.
class artical(models.Model):
    name = models.CharField(max_length=500000)
    title = models.CharField(max_length=500000)
    email = models.CharField(max_length=500000)
    art = models.TextField()
    def __str__(self):
        return self.email
class articals(models.Model):
    name = models.CharField(max_length=500000)
    title = models.CharField(max_length=500000)
    email = models.CharField(max_length=500000)
    art = models.TextField()
    def __str__(self):
        return self.email
class login(models.Model):
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    passw = models.CharField(max_length=100)
    def __str__(self):
        return self.email