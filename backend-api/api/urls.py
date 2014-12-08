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

        url(r'^categories/$',
            views.CategoryList.as_view(),
            name='category-list'),

        url(r'^degrees/$',
            views.DegreeList.as_view(),
            name='degree-list'),

        url(r'^degrees/(?P<pk>[0-9]+)/$',
            views.DegreeDetail.as_view(),
            name='degree-detail'),

        url(r'^degree-fields/$',
            views.DegreeFieldList.as_view(),
            name='degree-field-list'),

        url(r'^users/$',
            views.UserList.as_view(),
            name='user-list'),

        url(r'^users/(?P<pk>[0-9]+)/$',
            views.UserDetail.as_view(),
            name='user-detail'),

        url(r'^companies/$',
            views.CompanyList.as_view(),
            name='company-list'),

        url(r'^companies/(?P<pk>[0-9]+)/$',
            views.CompanyDetail.as_view(),
            name='company-detail'),

        url(r'^students/$',
            views.StudentList.as_view(),
            name='student-list'),

        url(r'^students/(?P<pk>[0-9]+)/$',
            views.StudentDetail.as_view(),
            name='student-detail'),

        url(r'^skill-levels/$',
            views.SkillLevelList.as_view(),
            name='skill-levels'),

        url(r'^cities/$',
            views.CityList.as_view(),
            name='city-list'),
))