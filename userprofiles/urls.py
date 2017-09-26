from django.conf.urls import url

from .views import DetailProfile

app_name = 'Profile'

urlpatterns = [
    url(r'^user/(?P<slug>[-\w ]+)/$', DetailProfile.as_view(), name='detail'),
]
