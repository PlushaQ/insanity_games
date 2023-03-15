from django.test import SimpleTestCase
from django.urls import reverse, resolve
from games.views import all_games, game_site

class TestUrls(SimpleTestCase):

    def test_all_games_url_is_resolved(self):
        url = reverse('games')
        self.assertEquals(resolve(url).func, all_games)

    def test_game_site_url_is_resolved(self):
        url = reverse('game', args=['game'])
        self.assertEquals(resolve(url).func, game_site)


