from django.conf.urls import include,url
from django.contrib import admin
from rest_framework import routers
from . import views
from .resources import api

router = routers.DefaultRouter()
#makes sure that the API endpoints work
router.register(r'races', views.RaceViewSet,'races')
router.register(r'racesparticipants',views.RaceParticipantViewSet,'racesparticipants')
router.register(r'particpants',views.ParticipantViewSet,'participants')
router.register(r'particpants',views.ParticipantViewSet,'participants')

urlpatterns = [
    url(r'^competitions/$', views.competitionview, name='competition'),
    url(r'^competitions/new$', views.new_competition, name='new_competition'),
    url(r'^competitions/(?P<pk>[0-9]+)/$', views.detail_competition, name='detail_competition'),
    url(r'^competitions/(?P<pk>[0-9]+)/task/new/$', views.new_task, name='new_task'),
    url(r'^competitions/(?P<competition>\w+)/task/(?P<task>\w+)/$', views.detail_task, name='detail_task'),
    url(r'^competitions/(?P<competition>\w+)/task/(?P<task>\w+)/send/(?P<participant>\w+)/$', views.send_participant, name='send_participant'),
    url(r'^competitions/(?P<competition>\w+)/task/(?P<task>\w+)/sendall/(?P<participant>\w+)/$', views.send_participants, name='send_participants'),

    url(r'^competitions/(?P<competition>\w+)/task/(?P<task>\w+)/rotate/(?P<participant>\w+)/$',views.rotate_galaxy, name='rotate_galaxy'),
    url(r'^competitions/(?P<competition>\w+)/task/(?P<task>\w+)/exitrotate/(?P<participant>\w+)/$', views.exit_rotate_galaxy,name='exit_rotate_galaxy'),

    url(r'^competitions/delete_competition/(?P<pk>\w+)/$', views.delete_competition),
    url(r'^competitions/(?P<competition>\w+)/task/delete_task/(?P<task>\w+)/$', views.delete_task),

    url(r'^air_races/$', views.airview, name='airrace'),
    url(r'^ground_races/$', views.groundview, name='groundrace'),
    url(r'^ground_races/race/new/$',views.new_race, name='new_race'),
    url(r'^air_races/race/new/$', views.new_airrace, name='new_airrace'),
    url(r'^ground_races/race/(?P<pk>[0-9]+)/$', views.detail_race, name='ground_detail_race'),
    url(r'^air_races/race/(?P<pk>[0-9]+)/$', views.detail_airrace, name='air_detail_race'),
    url(r'^ground_races/race/edit_race/(?P<pk>\w+)/$', views.edit_race),
    url(r'^air_races/race/edit_race/(?P<pk>\w+)/$', views.edit_airrace),
    url(r'^ground_races/race/delete_race/(?P<pk>\w+)/$', views.delete_race),
    url(r'^air_races/race/delete_race/(?P<pk>\w+)/$', views.delete_airrace),
    url(r'^create_participant/$',views.create_participant),
    url(r'^create_raceposition/$', views.create_raceposition),
    url(r'^ground_races/race/(?P<race>\w+)/send/(?P<participant>\w+)/$', views.ground_race_send, name='ground_race_send'),
    url(r'^air_races/race/(?P<race>\w+)/send/(?P<participant>\w+)/$', views.air_race_send,name='air_race_send'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(api.urls)),
    url(r'^api2', include(router.urls)),

]