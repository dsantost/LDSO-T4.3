from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views


urlpatterns = format_suffix_patterns(patterns('api.views',
        url(r'^institutions/$',
            views.InstitutionList.as_view(),
            name='institution-list'),

        url(r'^institutions/(?P<pk>[0-9]+)/$',
            views.InstitutionDetail.as_view(),
            name='institution-detail'),

        url(r'^degrees/$',
            views.DegreeList.as_view(),
            name='degree-list'),

        url(r'^degrees/(?P<pk>[0-9]+)/$',
            views.DegreeDetail.as_view(),
            name='degree-detail'),

        url(r'^users/$',
            views.UserList.as_view(),
            name='user-list'),

        url(r'^users/(?P<pk>[0-9]+)/$',
            views.UserDetail.as_view(),
            name='user-detail'),

        url(r'^cities/$',
            views.CityList.as_view(),
            name='city-list'),
))