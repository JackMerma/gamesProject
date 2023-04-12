from django.db import models

class Solution(models.Model):
    userName = models.CharField(max_length = 20) 
    idProblem = models.IntegerField() 
    solved = models.BooleanField(default = False)

