from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user
from django.contrib.auth.models import User
from django.utils import timezone

from main.models import News


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.test_news = News.objects.create(
            topic='Hey, it is me',
            text='a little of text is not harming anyone',
            publish_date=timezone.now()
        )

    def test_login_page_renders(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_redirects_to_homepage_after_correct_login(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpass'})
        self.assertRedirects(response, reverse('homepage'))

    def test_login_shows_error_after_providing_wrong_password(self):
        response = self.client.post(reverse('login'), {'username': 'wronguser', 'password': 'wrongpass'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Username or password is invalid.')

    def test_logout_logs_out_user_and_redirects_to_homepage(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('logout'))
        self.assertRedirects(response, reverse('homepage'))
        self.assertFalse('_auth_user_id' in self.client.session)

    def test_signup_page_renders_correctly(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_signup_with_valid_credentials_creates_user(self):
        response = self.client.post(reverse('signup'), {'username': 'testuser2', 'password': 'test1234!', 'password2': 'test1234!'})
        self.assertRedirects(response, reverse('homepage'))
        self.assertTrue(User.objects.filter(username='testuser2').exists())
        user = get_user(self.client)
        self.assertEqual(user.username, 'testuser2')

    def test_signup_with_invalid_credentials_shows_error_message(self):
        response = self.client.post(reverse('signup'), {'username': 'testuser2', 'password': 'password', 'password2': 'password'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Your password should be at least 8 characters and cointans 1 letter, 1 number and 1 symbol.")