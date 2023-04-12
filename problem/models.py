from django.db import models

class Problem(models.Model):
    userName = models.CharField(max_length = 20)
    description = models.TextField()
    difficulty = models.IntegerField()
    solved = models.BooleanField(default = False)
    hint = models.TextField()

