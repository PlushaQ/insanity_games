from django.test import SimpleTestCase
from django.urls import reverse, resolve
from opinions.views import all_opinions, add_opinion, single_opinion, delete_opinion

class TestUrls(SimpleTestCase):

    def test_all_opinions_url_resolves(self):
        url = reverse('all_opinions')
        self.assertEquals(resolve(url).func, all_opinions)

    def test_single_opinion_resolves(self):
        url = reverse('opinion', args=['1'])
        self.assertEquals(resolve(url).func, single_opinion)

    def test_add_opinion_url_resolves(self):
        url = reverse('add_opinion')
        self.assertEquals(resolve(url).func, add_opinion)

    def test_delete_opinion_url_resolves(self):
        url = reverse('delete_opinion', args=['1'])
        self.assertEquals(resolve(url).func, delete_opinion)
