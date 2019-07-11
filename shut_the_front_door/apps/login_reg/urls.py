# (?P<num>\d+)  accept number
# (?P<name>\w+)  accept char

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^show_register$', views.show_register),
    url(r'^profile$', views.success),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
]
