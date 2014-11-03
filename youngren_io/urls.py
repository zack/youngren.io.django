from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', include('apps.core.urls', namespace='apps.core')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^donations/', include('apps.donations.urls', namespace='apps.donations')),
)
