from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_games, name="games"),
    path('<slug:slug>', views.game_site, name="game"),
]
