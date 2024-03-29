from django.db import models
from django.utils.text import slugify
# Create your models here.


class Game(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=5000)
    slug = models.SlugField(max_length=255)
    short_description = models.TextField(max_length=255)
    cover = models.ImageField(upload_to='covers/')
    release_date = models.DateTimeField()
    genre = models.CharField(max_length=50)
    tags = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    def pretty_release_date(self):
        return self.release_date.strftime("%e %b %Y")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Game, self).save(*args, **kwargs)


