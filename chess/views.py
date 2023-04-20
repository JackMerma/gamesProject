from django.shortcuts import render, get_object_or_404
from .models import ChessProblem, ChessSolution
from .game.controller import create
import base64

def chessView(request,*args, **kargs):
    return render(request, 'chess.html')

def chessListView(request,*args, **kargs):
    queryset = ChessProblem.objects.all()
    context = {
        'objectList': queryset,
    }
    return render(request, 'chessProblemset.html', context)

def chessShowObjectView(request, myId):
    obj = get_object_or_404(ChessProblem, id = myId)
    code = ""
    error = ""

    # POST request
    if request.POST:
        code = request.POST["input"]

    # guardando imagen
    error = create(code, [str(request.user), str(myId)])

    # consultando por el objeto guardado
    try:
        solutionObject = ChessSolution.objects.get(userName = request.user, idProblem = myId)
        # si no es una peticion POST
        if not request.POST:
            code = solutionObject.codeChessSolution
    except:
        solutionObject = None


    context = {
        'object': obj,
        'objectSolution': solutionObject,
        'code': code,
        'error': error,
    }

    return render(request, 'chessProblemDescription.html', context)
