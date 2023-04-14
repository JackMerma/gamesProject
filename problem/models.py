from django.db import models
from django.urls import reverse

class Problem(models.Model):
    nameProblem = models.CharField(max_length = 20)
    description = models.TextField()
    difficulty = models.IntegerField()
    hint = models.TextField()

    def get_absolute_url(self):
        return reverse('browsing', kwargs = {'myId' : self.id})
