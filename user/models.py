from django.db import models

class Usuario(models.Model):
    names = models.ChartField(max_length = 50)
    surnames = models.TextField(max_length = 50)
    userName = models.TextField(max_length = 20)
    mail = models.EmailField(max_length = 254)
    birthdate = models.BirthdayField()
