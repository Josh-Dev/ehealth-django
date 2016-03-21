from django.conf.urls import patterns, url
from ehealth_project import views

urlpatterns = patterns('',
    url(r'^$', views.basic_search, name='basic_search'),
    url(r'^results',views.searchAll, name='results'),
    url(r'^about/$', views.about, name='about'),
    url(r'^how/$', views.how, name='how'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^user_finder/$', views.user_finder, name='user_finder'),
    url(r'^user_finder/?search_bar=(?P<query>[\w\-]+)/$', views.user_finder, name='user_finder_res'),
    url(r'^user_profile/(?P<username>[\w\-]+)/$',views.user_profile, name='user_profile'),
    url(r'^user_profile/(?P<username>[\w\-]+)/(?P<current_folder>[\w\-]+)/$',views.user_profile, name='user_profile'),
    url(r'^user_profile_form/$',views.user_profile_form,name='user_profile_form'),
    url(r'^advanced/$',views.advanced_search,name='advanced_search'),
    url(r'^saved_pages/$',views.saved_pages,name='saved_pages'),
    url(r'^manage_account/$',views.manage_account,name='manage_account'),
    url(r'^logout/$', views.user_logout, name='auth_logout'),
    url(r'^save_page/$', views.save_page, name='save_page'),
    url(r'^delete_folder/$', views.delete_folder, name='delete_folder'),
    url(r'^delete_folder/(?P<id>[\W\-]+)/$', views.delete_folder, name='delete_folder'),
    url(r'^delete_folder/(?P<id>[\w\-]+)/(?P<current_folder>[\w\-]+)/$', views.delete_folder, name='delete_folder')
)

