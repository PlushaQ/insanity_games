from django.test import TestCase
from datetime import datetime, timedelta
from main.models import News


class TestModels(TestCase):

    def setUp(self):
        self.news = News.objects.create(
            topic='Test News',
            text='This is a test news.',
            publish_date=datetime.now()
        )

    def test_str_method(self):
        self.assertEqual(str(self.news), 'Test News')

    def test_pretty_release_date_method(self):
        self.assertEqual(
                self.news.pretty_publish_date(),
                self.news.publish_date.strftime("%e %b %Y")
            )