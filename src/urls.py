# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url
from home.views import Index

urlpatterns = patterns('',
    url(r'^$', Index.as_view()),
)
