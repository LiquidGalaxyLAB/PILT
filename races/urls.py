from django.conf.urls import include,url
from django.contrib import admin
from rest_framework import routers
from . import views
from .resources import api

router = routers.DefaultRouter()
#makes sure that the API endpoints work
router.register(r'/races', views.RaceViewSet,'races')
router.register(r'/racesparticipants',views.RaceParticipantViewSet,'racesparticipants')
router.register(r'/particpants',views.ParticipantViewSet,'participants')

urlpatterns = [
    url(r'^air_races/$', views.airview, name='airrace'),
    url(r'^ground_races/$', views.groundview, name='groundrace'),
    url(r'^ground_races/race/new/$',views.new_race, name='new_race'),
    url(r'^air_races/race/new/$', views.new_race, name='new_race'),
    url(r'^ground_races/race/(?P<pk>[0-9]+)/$', views.detail_race, name='ground_detail_race'),
    url(r'^air_races/race/(?P<pk>[0-9]+)/$', views.detail_race, name='air_detail_race'),
    url(r'^ground_races/race/edit_race/(?P<pk>\w+)/$', views.edit_race),
    url(r'^air_races/race/edit_race/(?P<pk>\w+)/$', views.edit_race),
    url(r'^ground_races/race/delete_race/(?P<pk>\w+)/$', views.delete_race),
    url(r'^air_races/race/delete_race/(?P<pk>\w+)/$', views.delete_race),
    url(r'^create_participant/$',views.create_participant),
    url(r'^create_raceposition/$', views.create_raceposition),
    url(r'^ground_races/race/(?P<race>\w+)/send/(?P<participant>\w+)/$', views.ground_race_send, name='ground_race_send'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(api.urls)),
    url(r'^api2', include(router.urls)),

]