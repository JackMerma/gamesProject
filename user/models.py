from django.db import models

class User(models.Model):
    names = models.CharField(max_length = 50)
    surnames = models.CharField(max_length = 50)
    userName = models.CharField(max_length = 20)
    mail = models.EmailField(max_length = 254)
    birthdate = models.DateField()
