from django.db import models

class Problem(models.Model):
    description = models.TextField()
    hint = models.TextField()
    difficulty = models.IntegerField()
    solved = models.BooleanField(default = False)
