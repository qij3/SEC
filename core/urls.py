from django.conf.urls import patterns, include, url
from django.contrib import admin
import core.views as coreviews

urlpatterns = patterns('',

 url(r'^$', coreviews.LandingView.as_view()),
 url(r'team/$', coreviews.TeamListView.as_view()),
 url(r'team/(?P<pk>\d+)/detail/$', coreviews.TeamDetailView.as_view(), name='team_list'),
 url(r'team/create/$', coreviews.TeamCreateView.as_view()),
 url(r'team/(?P<pk>\d+)/update/$', coreviews.TeamUpdateView.as_view(), name='team_update'),

 url(r'profile/$', coreviews.ProfileListView.as_view()),
 url(r'profile/(?P<pk>\d+)/detail/$', coreviews.ProfileDetailView.as_view(), name='profile_list'),
 url(r'profile/create/$', coreviews.ProfileCreateView.as_view()),
 url(r'profile/(?P<pk>\d+)/update/$', coreviews.ProfileUpdateView.as_view(), name='profile_update'),


 url(r'team/(?P<pk>\d+)/profile/create/$', coreviews.ProfileCreateView.as_view(), name='profile_create'),
 url(r'team/(?P<pk>\d+)/profile/update/$', coreviews.ProfileUpdateView.as_view(), name='profile_update'),


 url(r'entrance/$', coreviews.entrance),
 url(r'logout/$', coreviews.logout_view),

)
