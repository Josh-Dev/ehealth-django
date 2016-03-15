from django.conf.urls import patterns, url
from ehealth_project import views

urlpatterns = patterns('',
    url(r'^$', views.basic_search, name='basic_search'),
    url(r'^about/$', views.about, name='about'),
    url(r'^how/$', views.how, name='how'),
    url(r'^register/$', views.register, name='register'),
    #url(r'^login/$', views.user_login, name='login'),
    #url(r'^user_finder', views.user_finder, name='user_finder'),
    url(r'^register/$', views.register, name='register'),
    url(r'^advanced',views.advanced_search,name='advanced_search'),
)
