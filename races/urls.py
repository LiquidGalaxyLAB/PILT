from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^air_race', views.airview, name='airrace'),
    url(r'^ground_race', views.groundview, name='groundrace'),
    url(r'^race/(?P<pk>[0-9]+)/$', views.detail_race,name='detail_race'),
    url(r'^race/new/$',views.new_race, name='new_race')
]