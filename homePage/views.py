from django.shortcuts import render
from django.http import HttpResponse

def homeView(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    context = {

    }
    return HttpResponse('Hola mundo')
