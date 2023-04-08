from django.shortcuts import render
from django.http import HttpResponse

def homeView(request, *args, **kwargs):
    context = {
        'user': request.user,
    }
    return render(request, 'home.html', context)
