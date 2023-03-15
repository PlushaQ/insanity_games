from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User

from opinions.models import Opinion


class OpinionModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass'
        )
        self.opinion = Opinion.objects.create(
            topic='Test topic',
            rating=3,
            message='This is a test message. It should be shortened here.',
            user=self.user,
            time=timezone.now()
        )

    def test_short_opinion(self):
        self.assertEqual(self.opinion.short_opinion(), 'This is a test message. It should be shortened her...')
        self.opinion.message = 'This is a short test message.'
        self.assertEqual(self.opinion.short_opinion(), 'This is a short test message.')

    def test_pretty_time(self):
        self.assertEqual(self.opinion.pretty_time(), self.opinion.time.strftime("%e %b %Y"))

    def test_opinion_creation(self):
        topic = 'Test topic'
        rating = 3
        message = 'Test message'
        time = timezone.now()

        opinion2 = Opinion.objects.create(
            topic=topic,
            rating=rating,
            message=message,
            user=self.user,
            time=time
        )

        self.assertEqual(opinion2.topic, topic)
        self.assertEqual(opinion2.rating, rating)
        self.assertEqual(opinion2.message, message)
        self.assertEqual(opinion2.user, self.user)
        self.assertEqual(opinion2.time, time)

        retrieved_opinion = Opinion.objects.get(id=opinion2.id)
        self.assertEqual(retrieved_opinion, opinion2)

    def test_opinion_fields_required(self):
        with self.assertRaises(Exception):
            Opinion.objects.create(user=self.user)

    def test_opinion_deletion(self):
        count_before = Opinion.objects.count()
        self.opinion.delete()
        count_after = Opinion.objects.count()
        self.assertEqual(count_before - 1, count_after)
        with self.assertRaises(Opinion.DoesNotExist):
            Opinion.objects.get(id=self.opinion.id)
