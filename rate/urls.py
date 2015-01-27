from django.conf.urls import patterns, url
from rate import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^link/(?P<link_title>[\w\-]+)/$', views.link),
        url(r'^create_link/$', views.create_link, name='create_link'),
)
