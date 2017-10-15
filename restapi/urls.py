from django.conf.urls import url, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.urlpatterns import format_suffix_patterns

from accounts.api.urls import accounts_api_urlpatterns
from comments.api.urls import comments_api_urlpatterns
from groups.api.urls import groups_api_urlpatterns
from items.api.urls import items_api_urlpatterns
from likes.api.urls import likes_api_urlpatterns

from restapi.CommentView.views import CommentAPIView
from restapi.ItemCardView.views import ItemCardAPIView, ItemCardListAPIView
from restapi.ItemDetailPage.views import ItemDetailPageAPIView, ItemDetailListAPIView

urlpatterns = [
    url(r'^commentview/$', CommentAPIView.as_view(), name='commentview'),
    url(r'^itemcardview/$', ItemCardListAPIView.as_view(), name='itemcardview-list'),
    url(r'^itemcardview/(?P<pk>\d+)/$', ItemCardAPIView.as_view(), name='itemcardview'),
    url(r'^itemdetailpage/$', ItemDetailListAPIView.as_view(), name='itemdetailpage-list'),
    url(r'^itemdetailpage/(?P<pk>\d+)/$', ItemDetailPageAPIView.as_view(), name='itemdetailpage'),
]

urlpatterns += accounts_api_urlpatterns
urlpatterns += comments_api_urlpatterns
urlpatterns += groups_api_urlpatterns
urlpatterns += items_api_urlpatterns
urlpatterns += likes_api_urlpatterns
urlpatterns = format_suffix_patterns(urlpatterns)
