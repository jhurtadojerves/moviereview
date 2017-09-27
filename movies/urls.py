from django.conf.urls import url

from .views import MovieList, MovieDetail, MovieUpdate, MovieCreate, ReviewCreate, ReviewUpdate

app_name = 'Movie'

urlpatterns = [
    url(r'^$', MovieList.as_view(), name='list'),
    url(r'^movie/add/$', MovieCreate.as_view(), name='create'),
    url(r'^movie/(?P<slug>[-\w ]+)/$', MovieDetail.as_view(), name='detail'),
    url(r'^movie/(?P<slug>[-\w ]+)/update/$', MovieUpdate.as_view(), name='update'),
    url(r'^movie/(?P<slug>[-\w ]+)/comment/update/$', ReviewUpdate.as_view(), name='review_update'),
]
