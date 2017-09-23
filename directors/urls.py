from django.conf.urls import url

from .views import DirectorList, DirectorDetail, DirectorCreate

app_name = 'Director'

urlpatterns = [
    url(r'^director/$', DirectorList.as_view(), name='list'),
    url(r'^director/add/$', DirectorCreate.as_view(), name='create'),
    url(r'^director/(?P<slug>[-\w ]+)/$', DirectorDetail.as_view(), name='detail'),
]