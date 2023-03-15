from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils import timezone
from main.views import homepage, about_us, contact_us, thanks, all_news
from games.models import Game
from main.models import News


class TestViews(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.homepage_url = reverse('homepage')
        self.about_us_url = reverse('about_us')
        self.contact_us_url = reverse('contact_us')
        self.thanks_url = reverse('thanks')
        self.all_news_url = reverse('news')
        self.test_game = Game.objects.create(
            title='test_game',
            description='A test game for testing purposes.',
            short_description='A test game',
            cover=SimpleUploadedFile("cover.jpg", b"content"),
            release_date=timezone.now(),
            genre='Action',
            tags='Test, Action'
        )
        self.test_news = News.objects.create(
            topic='Hey, it is me',
            text='a little of text is not harming anyone',
            publish_date=timezone.now()
        )

    def test_homepage_view(self):
        response = self.client.get(self.homepage_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'homepage.html')

    def test_homepage_variables(self):
        response = self.client.get(self.homepage_url)
        self.assertContains(response, self.test_news.topic)
        self.assertContains(response, self.test_news.text)

        self.assertContains(response, self.test_game.title)
        self.assertContains(response, self.test_game.short_description)

    def test_about_us_view(self):
        response = self.client.get(self.about_us_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'about_us.html')

    def test_contact_us_view(self):
        response = self.client.get(self.contact_us_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact_us.html')

    def test_thanks_view(self):
        response = self.client.get(self.thanks_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'thanks.html')

    def test_all_news_view(self):
        response = self.client.get(self.all_news_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'news.html')
