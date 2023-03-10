from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Opinion(models.Model):
    RATING_CHOICES = [
        (1, '1 star'),
        (2, '2 stars'),
        (3, '3 stars'),
        (4, '4 stars'),
        (5, '5 stars'),
    ]

    topic = models.CharField(max_length=255)
    rating = models.IntegerField(choices=RATING_CHOICES)
    message = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField()

    def __str__(self):
        return f"{self.topic} - {self.rating} stars by {self.user.username}"

    def short_opinion(self):
        if len(self.message) > 50:
            return self.message[:50] + '...'
        else:
            return self.message
