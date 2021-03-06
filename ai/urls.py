from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

import notification.urls

urlpatterns = patterns('',
                       url(r'^$', direct_to_template, {
            "template": "homepage.html",
            }, name="home"),
                       url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/img/favicon.ico'}),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^', include('articleflow.urls')),
                       url(r'^auth/', include('fancyauth.urls')),
                       url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}, name="auth_logout"),
                       url(r'^comments/', include('django.contrib.comments.urls')),
                       url(r'^issues/', include('issues.urls')),
                       url(r'^notes/', include('notes.urls')),
                       url(r'^errors/', include('errors.urls')),
                       url(r'^notifications/', include('notification.urls')),
                       )
