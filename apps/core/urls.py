from django.conf.urls import patterns, url
from apps.core import views

urlpatterns = patterns('',
    # Index view for youngren.io
    url(r'^$', views.index, name='index'),
)
