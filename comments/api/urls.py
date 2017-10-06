from django.conf.urls import url

from comments.api.views import (
    CommentReplyAPIView,
    CommentReplyDetailsAPIView,
    ImageCommentAPIView,
    ImageCommentDetailsAPIView,
    ItemCommentAPIView,
    ItemCommentDetailsAPIView,
    ProfileImageCommentAPIView,
    ProfileImageCommentDetailsAPIView,
)

comments_api_urlpatterns = [

    # comment/reply items, images, comments
    url(r'^comment/profile-image/$', ProfileImageCommentAPIView.as_view(), name='profile-image-comment'),

    url(r'^comment/profile-image/(?P<pk>\d+)/$', ProfileImageCommentDetailsAPIView.as_view(), name='profile-image-comment-details'),

    url(r'^comment/item/$', ItemCommentAPIView.as_view(), name='item-comment'),

    url(r'^comment/item/(?P<pk>\d+)/$', ItemCommentDetailsAPIView.as_view(), name='item-comment-details'),

    url(r'^comment/item-image/$', ImageCommentAPIView.as_view(), name='item-image-comment'),

    url(r'^comment/item-image/(?P<pk>\d+)/$', ImageCommentDetailsAPIView.as_view(), name='item-image-comment-details'),

    url(r'^comment/reply/$', CommentReplyAPIView.as_view(), name='comment-reply'),

    url(r'^comment/reply/(?P<pk>\d+)/$', CommentReplyDetailsAPIView.as_view(), name='comment-reply-details'),
]
