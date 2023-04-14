from django.shortcuts import render, get_object_or_404
from .models import ChessProblem

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
    context = {
        'object': obj,
    }
    return render(request, 'chessProblemDescription.html', context)

