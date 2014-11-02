from django.conf.urls import patterns, url
from apps.donations import views

urlpatterns = patterns('',
    # ex: /donations/
    url(r'^$', views.index, name='index'),
    # ex: /donations/5/
    url(r'^(?P<donation_id>\d+)/$', views.detail, name='detail'),
)
