from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^donations/', include('apps.donations.urls', namespace='apps.donations')),
    url(r'^admin/', include(admin.site.urls)),
)
