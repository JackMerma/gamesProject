from django.shortcuts import render, get_object_or_404
from .models import ChessProblem
from .game.controller import create

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

    # GET request
    if request.GET:
        code = request.GET["input"]

    output = create(code, [str(request.user), str(myId)])
    error = output[1]

    context = {
        'object': obj,
        'code': code,
        'error': error,
    }

    return render(request, 'chessProblemDescription.html', context)
