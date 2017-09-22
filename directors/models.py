from django.db import models
from autoslug import AutoSlugField

# Create your models here.

class Director(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    slug = AutoSlugField(unique=True, populate_from='get_full_name', always_update=True)
    birthday = models.DateField()

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.get_full_name()

