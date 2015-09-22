"""datavizweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
"""
Author : Soumyaranjan
Email : soumya.raula@gmail.com
Created : 19 Sep 2015

"""
from django.conf.urls import patterns,include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^userdata/', include('userdataviz.urls')),
    url(r'^login/$', 'datavizweb.views.login'),
    url(r'^auth/$', 'datavizweb.views.auth_view'),
    url(r'^logout/$', 'datavizweb.views.logout'),
    url(r'^loggedin/$', 'datavizweb.views.loggedin'),
    url(r'^invalid/$', 'datavizweb.views.invalid_login'),
    url(r'^register/$', 'datavizweb.views.register_user'),
    url(r'^register_success/$', 'datavizweb.views.register_success'),

)
