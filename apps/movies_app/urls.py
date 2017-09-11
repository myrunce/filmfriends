from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.login_reg),
    url(r'^process$', views.process),
    url(r'^login$', views.login),
    url(r'^welcome/?$', views.welcome),
    url(r'^look$', views.look),
    url(r'^add/(?P<root_id>\d+)/(?P<movie_title>\w+)/(?P<theatre>\w+)$', views.addMovie),
    url(r'^moviesAttending$', views.moviesAttending),
    url(r'^logout$', views.logout),
    url(r'^delete/(?P<movie_id>\d+)$', views.delete),
    url(r'^whosGoing/(?P<movie_id>\d+)$', views.whosGoing),    
]
