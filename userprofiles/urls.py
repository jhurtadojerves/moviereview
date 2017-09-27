from django.conf.urls import url

from .views import DetailProfile, SignUpView, SignInView, SignOutView, UpdateProfile

app_name = 'Profile'

urlpatterns = [
    url(r'^user/(?P<slug>[-\w ]+)/$', DetailProfile.as_view(), name='detail'),
    url(r'^user/(?P<slug>[-\w ]+)/update/$', UpdateProfile.as_view(), name='update'),
    url(r'^signup/$', SignUpView.as_view(), name='sign_up'),
    url(r'^signin/$', SignInView.as_view(), name='sign_in'),
    url(r'^signout/$', SignOutView.as_view(), name='sign_out'),
]
