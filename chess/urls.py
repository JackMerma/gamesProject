from django.urls import path
from . import views

urlpatterns = [
    #Url donde se mostraran las piezas
    #una breve explicacion
    path('', views.chessView, name='Chess'),

    #Url donde se mostrara el listado de problemas
    path('problemset/', views.chessListView, name='ChessList'),

    #Url para mostrar la descripcion de cada problema
    path('problem/<int:myId>/', views.chessShowObjectView, name = 'browsing')
]
