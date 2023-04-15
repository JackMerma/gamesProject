from django.db import models
from problem.models import Problem
from solution.models import Solution

class ChessProblem(Problem):
    imageChessProblem = models.ImageField(null=True, blank=True)
    fileChessProblem = models.FileField(null=True, blank=True)

class ChessSolution(Solution):
    codeChessSolution = models.TextField()
    imageChessSolution = models.ImageField(null=True, blank=True, upload_to='images/chessSolutions/')
    fileChessSolution = models.FileField(null=True, blank=True)
