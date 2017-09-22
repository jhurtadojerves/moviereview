from django.conf.urls import url

from .views import MovieList

app_name = 'Movie'

urlpatterns = [
    url(r'^$', MovieList.as_view(), name='list'),
]
