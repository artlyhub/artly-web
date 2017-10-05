from django.conf.urls import url

from comments.api.views import (
    CommentReplyAPIView,
    CommentReplyDetailsAPIView,
    ImageCommentAPIView,
    ImageCommentDetailsAPIView,
    ItemCommentAPIView,
    ItemCommentDetailsAPIView,
)

comments_api_urlpatterns = [

    # comment/reply items, images, comments
    url(r'^comment/item/$', ItemCommentAPIView.as_view(), name='item-comment'),

    url(r'^comment/item/(?P<pk>\d+)/$', ItemCommentDetailsAPIView.as_view(), name='item-comment-details'),

    url(r'^comment/image/$', ImageCommentAPIView.as_view(), name='image-comment'),

    url(r'^comment/image/(?P<pk>\d+)/$', ImageCommentDetailsAPIView.as_view(), name='image-comment-details'),

    url(r'^comment/reply/$', CommentReplyAPIView.as_view(), name='comment-reply'),

    url(r'^comment/reply/(?P<pk>\d+)/$', CommentReplyDetailsAPIView.as_view(), name='comment-reply-details'),
]
