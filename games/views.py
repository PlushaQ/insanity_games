from django.shortcuts import render, get_object_or_404
from .models import Game
# Create your views here.


def all_games(request):
    games = Game.objects
    return render(request, 'games.html', {'games': games})


def game_site(request, slug):
    game = get_object_or_404(Game, slug=slug)
    return render(request, 'game.html', {'game': game})
