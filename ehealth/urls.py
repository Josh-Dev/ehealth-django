from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    #Urls

    url(r'^admin/', include(admin.site.urls)),
    url(r'^ehealth/', include('ehealth_project.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls'))
)
