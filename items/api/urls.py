from django.conf.urls import url, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.urlpatterns import format_suffix_patterns

from items.api.views import (
    ImageAPIView,
    ImageDetailsAPIView,
    ItemAPIView,
    ItemDetailsAPIView,
)

items_api_urlpatterns = [

    # user uploaded images (related to items)
    url(r'^item-image/$', ImageAPIView.as_view(), name="item-image"),

    url(r'^item-image/(?P<pk>\d+)/$',
        ImageDetailsAPIView.as_view(), name="item-image-details"),


    # user uploaded items
    url(r'^item/$', ItemAPIView.as_view(), name="item"),

    url(r'^item/(?P<pk>\d+)/$',
        ItemDetailsAPIView.as_view(), name="item-details"),
]
