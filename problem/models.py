from django.db import models

class Problem(models.Model):
    nameProblem = models.CharField(max_length = 20) 
    description = models.TextField()
    difficulty = models.IntegerField()
    hint = models.TextField()

