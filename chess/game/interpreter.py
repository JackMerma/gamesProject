from .colors import *
from PIL import Image
from chess.models import ChessSolution
import os
from pathlib import Path
from django.core.files import File

SIZE = 464
BASE_DIR = Path(__file__).resolve().parent.parent

def putPixels(img, picture):
    for i in range(SIZE):
        for j in range(SIZE):
            if i >= len(picture.img) or j >= len(picture.img[i]):
                img.putpixel((j, i), BACKGROUND_COLOR)
            else:
                img.putpixel((j, i), color[picture.img[i][j]])

    return img


def draw(data):
    picture = data[0]
    userName = data[1]
    problemId = data[2]
    oldCode = data[3]

    # genera la imagen
    img = Image.new('RGB', (SIZE, SIZE))
    img = putPixels(img, picture)
    file_name = userName + problemId + ".jpg"
    path = os.path.join(BASE_DIR, "static/images/" + file_name)
    img.save(path)

    # guardando en la bd
    try:
        lastSolution = ChessSolution.objects.get(userName = data[1], idProblem = int(data[2]))
    except:
        lastSolution = None

    if lastSolution:
        if lastSolution.imageChessSolution:
            lastSolution.imageChessSolution.delete()
    else:
        lastSolution = ChessSolution.objects.create(userName = data[1], idProblem = int(data[2]))

    with open(path, 'rb') as image_file:
        file = File(image_file)
        lastSolution.imageChessSolution.save(file_name, file)
    lastSolution.codeChessSolution = oldCode
    lastSolution.save()

    # eliminando de static
    if os.path.exists(path):
        os.remove(path)
