from django.conf.urls import patterns, include, url
from django.contrib import admin
import core.views as coreviews

from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',

 url(r'^$', coreviews.LandingView.as_view()),
 url(r'team/$', coreviews.TeamListView.as_view()),
 url(r'team/(?P<pk>\d+)/detail/$', coreviews.TeamDetailView.as_view(), name='team_list'),
 url(r'team/create/$', login_required(coreviews.TeamCreateView.as_view())),
 url(r'team/(?P<pk>\d+)/update/$', login_required(coreviews.TeamUpdateView.as_view()), name='team_update'),

 url(r'profile/$', coreviews.ProfileListView.as_view()),
 url(r'profile/(?P<pk>\d+)/detail/$', coreviews.ProfileDetailView.as_view(), name='profile_list'),
 url(r'profile/create/$', login_required(coreviews.ProfileCreateView.as_view())),
 url(r'profile/(?P<pk>\d+)/update/$', login_required(coreviews.ProfileUpdateView.as_view()), name='profile_update'),


 url(r'signup/$', coreviews.register),
 url(r'login/$', coreviews.user_login),
 url(r'logout/$', coreviews.logout_view),

)
