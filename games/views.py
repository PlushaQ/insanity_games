from django.shortcuts import render, get_object_or_404
from .models import Games
# Create your views here.


def all_games(request):
    games = Games.objects
    return render(request, 'games.html', {'games': games})


def game_site(request, title):
    game = get_object_or_404(Games, title=title)
    return render(request, 'game.html', {'game': game})
