from django.contrib import admin

from .models import Movie, Review

# Register your models here.


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Review)
class RevewAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie', 'user', 'rating', )
