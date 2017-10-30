from django.conf.urls import url

from groups.api.views import (
    GroupAPIView,
    GroupDetailsAPIView,
    GroupImageAPIView,
    GroupImageDetailsAPIView,
)

groups_api_urlpatterns = [

    # group creation, updates
    url(r'^group/$', GroupAPIView.as_view(), name='group'),

    url(r'^group/(?P<pk>\d+)/$',
        GroupDetailsAPIView.as_view(), name="group-details"),

    url(r'^group-image/$',
        GroupImageAPIView.as_view(), name="group-image"),

    url(r'^group-image/(?P<pk>\d+)/$',
        GroupImageDetailsAPIView.as_view(), name="group-image-details"),
]
