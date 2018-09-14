# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from . import views


urlpatterns = [
    # Index
    url(r'^$', views.index, name='index'),
    # Pages
    url(r'^binary_search', views.binary_search, name='binary_search'),
]
