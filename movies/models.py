from django.db import models
from autoslug import AutoSlugField
from django.core.validators import MaxValueValidator, MinValueValidator

from directors.models import Director
from userprofiles.models import Profile

# Create your models here.


class Movie(models.Model):
    title = models.TextField(blank=False, unique=True)
    synopsis = models.TextField(blank=False)
    author = models.ForeignKey(Profile, related_name='movies')
    director = models.ForeignKey(Director, related_name='movies')
    created_date = models.DateField(auto_now_add=True)
    slug = AutoSlugField(unique=True, populate_from='title', always_update=True)
    cover = models.ImageField(default='none.png')
    star = models.ManyToManyField(Profile, through='Review')

    def __str__(self):
        return self.title


class Review(models.Model):
    movie = models.ForeignKey(Movie)
    user = models.ForeignKey(Profile)
    comment = models.TextField()
    rating = models.IntegerField(default=1,
                                 validators=[
                                     MinValueValidator(1),
                                     MaxValueValidator(5),
                                 ])
    created_date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('movie', 'user', )

