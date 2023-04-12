from django.urls import path
from . import views

urlpatterns = [
    #Url donde se mostraran las piezas
    #una breve explicacion
    path('', views.chessView, name='Chess'),

    #Url donde se mostrara el listado de problemas
    path('list/', views.chessListView, name='ChessList'),
]
