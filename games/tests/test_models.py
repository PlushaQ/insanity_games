from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils import timezone

from games.models import Game


class TestModels(TestCase):
    def setUp(self) -> None:
        self.test_game = Game.objects.create(
            title='Test Game',
            description='A test game for testing purposes.',
            short_description='A test game',
            cover=SimpleUploadedFile("cover.jpg", b"content"),
            release_date=timezone.now(),
            genre='Action',
            tags='Test, Action'
        )

    def test_name_is_assigned_a_slug_on_creation(self):
        self.assertEqual(self.test_game.slug, 'test-game')

    def test_str_method(self):
        self.assertEqual(str(self.test_game), 'Test Game')

    def test_pretty_release_date_method(self):
        self.assertEqual(
                self.test_game.pretty_release_date(),
                self.test_game.release_date.strftime("%e %b %Y")
            )



