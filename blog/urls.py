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
    url(r'^$', views.post_list, name='post_list'),
]
