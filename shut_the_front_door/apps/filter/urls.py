# (?P<num>\d+)  accept number
# (?P<name>\w+)  accept char

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    # route to profile.html interprets form info
    url(r'^create_filter$', views.create_filter),
    url(r'^display_create_filter$', views.display_create_filter),
    url(r'^request$', views.dic_json),
    url(r'^delete_filter/(?P<id>\d+)$', views.delete_filter),
]
