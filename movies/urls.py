from django.conf.urls import url
from . import views as def_views
from django.contrib.auth import views as auth_views

app_name = 'movies'

urlpatterns = [
    url(r'^$', def_views.home, name='home'),
    url(r'^index$', def_views.index, name='index'),
    url(r'^(?P<movie_id>[0-9]+)/$', def_views.details, name='details'),
    url(r'^(?P<pk>[0-9]+)/comment/$', def_views.add_comment, name='add_comment'),
    url(r'^(?P<pk>[0-9]+)/comment/delete/$', def_views.delete_comment, name='delete_comment'),
    url(r'^register/$', def_views.signup, name='signup'),
    url(r'^login/$', auth_views.login, {'template_name': 'movies/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/movies/index'}, name='logout'),






]
