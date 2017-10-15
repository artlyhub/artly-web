from django.conf.urls import url

from likes.api.views import (
    LikeCommentAPIView,
    LikeGroupAPIView,
    LikeImageAPIView,
    LikeItemAPIView,
    LikeProfileImageAPIView,
    LikeReplyAPIView,
)

likes_api_urlpatterns = [

    # like/unlike profile images, items, images, comments, replies
    url(r'^like/profile-image/$', LikeProfileImageAPIView.as_view(), name='profile-image-like'),

    url(r'^like/item/$', LikeItemAPIView.as_view(), name='item-like'),

    url(r'^like/item-image/$', LikeImageAPIView.as_view(), name='item-image-like'),

    url(r'^like/group/$', LikeGroupAPIView.as_view(), name='group-like'),

    url(r'^like/comment/$', LikeCommentAPIView.as_view(), name='comment-like'),

    url(r'^like/reply/$', LikeReplyAPIView.as_view(), name='reply-like'),
]
