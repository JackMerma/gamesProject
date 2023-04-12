from django.db import models
from problem.models import Problem

class ChessProblem(Problem):
    imageSolution = models.ImageField(null=True, blank=True)
    imageSubmit = models.ImageField(null=True, blank=True)
    fileSolution = models.FileField(null=True, blank=True)
    fileSubmit = models.FileField(null=True, blank=True)
