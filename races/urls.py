from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^air_race', views.airview, name='airrace'),
    url(r'^ground_race', views.groundview, name='groundrace'),
]