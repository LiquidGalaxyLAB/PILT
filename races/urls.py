from django.conf.urls import include,url
from django.contrib import admin
from rest_framework import routers
from . import views
from .resources import api

router = routers.DefaultRouter()
#makes sure that the API endpoints work
router.register(r'races', views.RaceViewSet,'races')

urlpatterns = [
    url(r'^air_race/$', views.airview, name='airrace'),
    url(r'^ground_race/$', views.groundview, name='groundrace'),
    url(r'^ground_race/race/new/$',views.new_race, name='new_race'),
    url(r'^air_race/race/new/$', views.new_race, name='new_race'),
    url(r'^ground_race/race/(?P<pk>[0-9]+)/$', views.detail_race, name='detail_race'),
    url(r'^air_race/race/(?P<pk>[0-9]+)/$', views.detail_race, name='detail_race'),
    url(r'^ground_race/race/edit_race/(?P<pk>\w+)/$', views.edit_race),
    url(r'^air_race/race/edit_race/(?P<pk>\w+)/$', views.edit_race),
    url(r'^ground_race/race/delete_race/(?P<pk>\w+)/$', views.delete_race),
    url(r'^air_race/race/delete_race/(?P<pk>\w+)/$', views.delete_race),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #url(r'^api/', include(api.urls)),
     url(r'^', include(router.urls)),

]