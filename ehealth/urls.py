from django.conf.urls import patterns, include, url
from django.contrib import admin
from registration.backends.simple.views import RegistrationView

# Create a new class that redirects the user to the index page, if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(self,request, user):
        return '/ehealth/'


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ehealth/', include('ehealth_project.urls')),
        #Add in this url pattern to override the default pattern in accounts.
    url(r'^accounts/', include('registration.backends.simple.urls')),
)
