from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^air_race/$', views.airview, name='airrace'),
    url(r'^ground_race/$', views.groundview, name='groundrace'),
    url(r'^ground_race/race/new/$',views.new_race, name='new_race'),
    url(r'^air_race/race/new/$', views.new_race, name='new_race'),
    url(r'^ground_race/race/(?P<pk>[0-9]+)/$', views.detail_race, name='detail_race'),
    url(r'^air_race/race/(?P<pk>[0-9]+)/$', views.detail_race, name='detail_race'),

    url(r'^race/delete_race/(?P<pk>\w+)/$', views.delete_race),

]