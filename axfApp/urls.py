from django.conf.urls import url
from axfApp import views

urlpatterns = [
    url(r'^index/$', views.index),
]