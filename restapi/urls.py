from django.conf.urls import url, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.urlpatterns import format_suffix_patterns

from accounts.api.urls import accounts_api_urlpatterns
from comments.api.views import (
    CommentReplyAPIView,
    CommentReplyDetailsAPIView,
    ImageCommentAPIView,
    ImageCommentDetailsAPIView,
    ItemCommentAPIView,
    ItemCommentDetailsAPIView,
)
from items.api.urls import items_api_urlpatterns
from likes.api.views import (
    LikeCommentAPIView,
    LikeImageAPIView,
    LikeItemAPIView,
    LikeReplyAPIView,
)
from restapi.ItemCardView.views import ItemCardAPIView

urlpatterns = [
    # like/unlike items, images
    url(r'^like/item/$', LikeItemAPIView.as_view(), name='item-like'),
    url(r'^like/image/$', LikeImageAPIView.as_view(), name='image-like'),
    url(r'^like/comment/$', LikeCommentAPIView.as_view(), name='comment-like'),
    url(r'^like/reply/$', LikeReplyAPIView.as_view(), name='reply-like'),

    # comment/reply items, images, comments
    url(r'^comment/item/$', ItemCommentAPIView.as_view(), name='item-comment'),
    url(r'^comment/item/(?P<pk>\d+)/$', ItemCommentDetailsAPIView.as_view(), name='item-comment-details'),
    url(r'^comment/image/$', ImageCommentAPIView.as_view(), name='image-comment'),
    url(r'^comment/image/(?P<pk>\d+)/$', ImageCommentDetailsAPIView.as_view(), name='image-comment-details'),
    url(r'^comment/reply/$', CommentReplyAPIView.as_view(), name='comment-reply'),
    url(r'^comment/reply/(?P<pk>\d+)/$', CommentReplyDetailsAPIView.as_view(), name='comment-reply-details'),

    url(r'^itemcardview/(?P<pk>\d+)/$', ItemCardAPIView.as_view(), name='itemcardview'),
]

urlpatterns += accounts_api_urlpatterns
urlpatterns += items_api_urlpatterns
urlpatterns = format_suffix_patterns(urlpatterns)
