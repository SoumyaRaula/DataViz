"""
Author : Soumyaranjan
Email : soumya.raula@gmail.com
Created : 19 Sep 2015

"""
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^all/$', 'userdataviz.views.user_fetch_all_data'),
                       url(r'^get/(?P<uploaded_id>\d+)/$', 'userdataviz.views.user_current_data'),
    )