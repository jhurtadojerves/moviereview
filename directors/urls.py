from django.conf.urls import url

from .views import DirectorList, DirectorDetail

app_name = 'Director'

urlpatterns = [
    url(r'^director/$', DirectorList.as_view(), name='list'),
    url(r'^director/(?P<slug>[-\w ]+)/$', DirectorDetail.as_view(), name='detail'),
]