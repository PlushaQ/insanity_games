from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import homepage, about_us, all_news, contact_us, thanks


class TestUrls(SimpleTestCase):

    def test_homepage_url_resolves(self):
        url = reverse('homepage')
        self.assertEquals(resolve(url).func, homepage)

    def test_about_us_resolves(self):
        url = reverse('about_us')
        self.assertEquals(resolve(url).func, about_us)

    def test_all_news_url_resolves(self):
        url = reverse('news')
        self.assertEquals(resolve(url).func, all_news)

    def test_contact_us_url_resolves(self):
        url = reverse('contact_us')
        self.assertEquals(resolve(url).func, contact_us)

    def test_thanks_url_resolves(self):
        url = reverse('thanks')
        self.assertEquals(resolve(url).func, thanks)

