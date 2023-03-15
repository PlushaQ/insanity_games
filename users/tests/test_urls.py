from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users.views import login, logout, signup

class TestUrls(SimpleTestCase):

    def test_login_url_resolves(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, login)

    def test_logout_url_resolves(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logout)

    def test_signup_url_resolves(self):
        url = reverse('signup')
        self.assertEquals(resolve(url).func, signup)

