from django.db import models
from autoslug import AutoSlugField

from directors.models import Director
from userprofiles.models import Profile

# Create your models here.


class Movie(models.Model):
    title = models.TextField(blank=False)
    review = models.TextField(blank=False)
    author = models.ForeignKey(Profile, related_name='movies')
    director = models.ForeignKey(Director, related_name='movies')
    created_date = models.DateField(auto_now_add=True)
    slug = AutoSlugField(unique=True, populate_from='title', always_update=True)

    def __str__(self):
        return self.title
