from django.db import models

# Create your models here.


class News(models.Model):
    topic = models.CharField(max_length=100)
    text = models.TextField()
    publish_date = models.DateField()

    def __str__(self):
        return self.topic

    def pretty_publish_date(self):
        return self.publish_date.strftime("%e %b %Y")
