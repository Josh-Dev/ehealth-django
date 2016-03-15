from django.conf.urls import patterns, url
from ehealth_project import views

urlpatterns = patterns('',
    url(r'^$', views.search, name='search'),
    #url(r'^about/$', views.about, name='about'),
    url(r'^register/$', views.register, name='register'),
    #url(r'^login/$', views.user_login, name='login'),
    #url(r'^user_finder', views.user_finder, name='user_finder'),
    url(r'^register/$', views.register, name='register'),
    url(r'^advanced',
        views.advanced_search,
        name='advanced_search'),
)
