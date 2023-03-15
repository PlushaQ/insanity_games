from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

from opinions.models import Opinion


class TestViews(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass'
        )
        self.opinion = Opinion.objects.create(
            topic='Test topic',
            rating=3,
            message='Test message',
            user=self.user,
            time=timezone.now()
        )

    def test_all_opinions_view(self):
        response = self.client.get(reverse('all_opinions'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('all_opinions.html')
        self.assertContains(response, 'Test topic')
        self.assertContains(response, 'Test message')

    def test_single_opinion_view(self):
        response = self.client.get(reverse('opinion', args=[self.opinion.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('opinion.html')
        self.assertContains(response, 'Test topic')
        self.assertContains(response, 'Test message')

    def test_add_opinion_view(self):
        self.client.login(username='testuser', password='testpass')
        form_data = {
            'topic': 'New topic',
            'rating': 4,
            'message': 'New message'
        }
        response = self.client.post(reverse('add_opinion'), form_data)
        self.assertTemplateUsed('add_opinion.html')
        self.assertRedirects(response, reverse('all_opinions'))
        self.assertEqual(Opinion.objects.count(), 2)

        new_opinion = Opinion.objects.last()

        self.assertEqual(new_opinion.topic, 'New topic')
        self.assertEqual(new_opinion.rating, 4)
        self.assertEqual(new_opinion.message, 'New message')
        self.assertEqual(new_opinion.user, self.user)

    def test_delete_opinion_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('delete_opinion', args=[self.opinion.id]))
        self.assertRedirects(response, reverse('all_opinions'))
        self.assertEqual(Opinion.objects.count(), 0)
