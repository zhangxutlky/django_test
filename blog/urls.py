#########################################################################
# File Name: urls.py
# Author: Xu Zhang
# Email: xuzhang@cs.unm.edu
# Created Time: Thu 02 Nov 2017 03:16:32 PM MDT
#########################################################################
#!/usr/bin/python
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^blog/$', views.post_list, name='post_list'),
    url(r'^article/(?P<article_id>[0-9]+)$', views.article_page, name='article_page'),
    url(r'^edit/(?P<article_id>[0-9]+)$', views.edit_page, name = 'edit_page'),
    url(r'^edit/action$', views.edit_action, name='edit_action'),
]
