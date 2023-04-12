from django.shortcuts import render

# Create your views here.

def chessView(request,*args, **kargs):
    return render(request, 'chess.html')

def chessListView(request,*args, **kargs):
    return render(request, 'chess.html')

