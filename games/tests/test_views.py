from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils import timezone

from games.models import Game


class TestViews(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.games_url = reverse('games')
        self.game_url = reverse('game', args=['test_game'])
        self.test_game = Game.objects.create(
            title='test_game',
            description='A test game for testing purposes.',
            short_description='A test game',
            cover=SimpleUploadedFile("cover.jpg", b"content"),
            release_date=timezone.now(),
            genre='Action',
            tags='Test, Action'
        )

    def test_all_game_view(self):
        response = self.client.get(self.games_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'games.html')

    def test_game_view(self):
        response = self.client.get(self.game_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'game.html')
