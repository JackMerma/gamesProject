from .colors import *
from PIL import Image
from chess.models import *
import os
from pathlib import Path
from django.core.files import File

SIZE = 464
BASE_DIR = Path(__file__).resolve().parent.parent

# function que dibuja pixeles en un tipo de dato Image
def putPixels(img, picture):
    for i in range(SIZE):
        for j in range(SIZE):
            # para el fondo
            if i >= len(picture.img) or j >= len(picture.img[i]):
                img.putpixel((j, i), BACKGROUND_COLOR)
            # para las fichas
            else:
                img.putpixel((j, i), color[picture.img[i][j]])
    return img

# function alterada (parametros)
# mientras que el usuario debe saber que draw recibe un objecto de tipo picture
# verdaderamente se recibe una lista de datos (incluido el objeto picture)
# esto se hace para realizar otros procedimientos (esta alteracion se hace en controller.py)
def draw(data):
    # data recibida en controller
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

    #guardar texto generado en archivo
    file_text_name = userName + problemId + ".txt"
    text_image = picture._printImage()
    path_text = os.path.join(BASE_DIR, "static/texts/" + file_text_name)
    with open(path_text, "w") as chessFileText :
        chessFileText.write(text_image)
        calculatePorcentage(path_text, problemId)


    # guardando en la bd
    try:
        lastSolution = ChessSolution.objects.get(userName = data[1], idProblem = int(data[2]))
    except:
        lastSolution = None

    if lastSolution:
        if lastSolution.imageChessSolution:
            lastSolution.imageChessSolution.delete()
        if lastSolution.fileChessSolution:
            lastSolution.fileChessSolution.delete()
    else:
        lastSolution = ChessSolution.objects.create(userName = data[1], idProblem = int(data[2]))

    with open(path, 'rb') as image_file:
        file = File(image_file)
        lastSolution.imageChessSolution.save(file_name, file)

    with open(path_text, 'rb') as text_file:
        file = File(text_file)
        lastSolution.fileChessSolution.save(file_text_name, file)

    lastSolution.codeChessSolution = oldCode
    lastSolution.save()

    # eliminando la imagen y texto generada de static
    if os.path.exists(path):
        os.remove(path)
    if os.path.exists(path_text):
        os.remove(path_text)

def calculatePorcentage(path_text_solution,problemId):
    try:
        problemSolution = ChessProblem.objects.get(id = int(problemId))
    except:
        problemSolution = None

    print("url: " + problemSolution.fileChessProblem.url)
    #ruteAux = os.path.join(BASE_DIR, "static" + problemSolution.fileChessProblem.url)
    ruteAux = "/home/darwin/gameProject/gamesProject/media" + problemSolution.fileChessProblem.url
    print("ruta mediante ruteAux: " + ruteAux)
    print("ruta argumento:  " + path_text_solution)

    with open(path_text_solution, 'r') as file1:
        lines1 = file1.readlines()

    with open(ruteAux, 'r') as file2:
        lines2 = file2.readlines()

    if len(lines1) != len(lines2):
        print('Los archivos no tienen la misma cantidad de líneas')
    else:
        coincidencias = 0
        for line1, line2 in zip(lines1, lines2):
            if line1 == line2:
                coincidencias += 1

        porcentaje = coincidencias / len(lines1) * 100
        print(f'El porcentaje de coincidencia entre los archivos es: {porcentaje}%')

