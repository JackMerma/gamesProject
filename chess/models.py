from django.db import models
from problem.models import Problem
from solution.models import Solution

class ChessProblem(Problem):
    imageChessProblem = models.ImageField(null=True, blank=True)
    fileChessProblem = models.FileField(null=True, blank=True)

class ChessSolution(Solution):
    imageChessSolution = models.BinaryField()
    fileChessSolution = models.FileField(null=True, blank=True)
