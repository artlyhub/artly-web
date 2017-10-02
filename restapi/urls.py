from django.conf.urls import url, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.urlpatterns import format_suffix_patterns

from accounts.api.views import (
    FollowerAPIView,
    FollowerAddAPIView,
    ProfileAPIView,
    ProfileImageAPIView,
    ProfileImageDetailsAPIView,
    ProfileDetailsAPIView,
    UserAPIView,
    UserDetailsAPIView,
    UserProfileImageAPIView,
    UserItemAPIView,
    UserLoginAPIView,
)
from comments.api.views import (
    CommentReplyAPIView,
    CommentReplyDetailsAPIView,
    ImageCommentAPIView,
    ImageCommentDetailsAPIView,
    ItemCommentAPIView,
    ItemCommentDetailsAPIView,
)
from items.api.views import (
    ImageAPIView,
    ImageDetailsAPIView,
    ItemAPIView,
    ItemDetailsAPIView,
    ItemFullAPIView,
)
from likes.api.views import (
    LikeCommentAPIView,
    LikeImageAPIView,
    LikeItemAPIView,
    LikeReplyAPIView,
)
from records.api.views import RecordAPIView
from restapi.ItemCardView.views import ItemCardAPIView

urlpatterns = {
    # token maker
    url(r'^get-token/', obtain_auth_token),

    # basic user login, info urls
    url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
    url(r'^user/$', UserAPIView.as_view(), name="user"),
    url(r'^user/(?P<username>[\w.@+-]+)/$',
        UserDetailsAPIView.as_view(), name="user-details"),

    # user profile related urls
    url(r'^profile/$', ProfileAPIView.as_view(), name="profile"),
    url(r'^profile/(?P<pk>[\w.@+-]+)/$',
        ProfileDetailsAPIView.as_view(), name="profile-details"),
    url(r'^profile/(?P<pk>[\w.@+-]+)/followers/$',
        FollowerAPIView.as_view(), name="followers"),
    url(r'^profile/(?P<pk>[\w.@+-]+)/items/$',
        UserItemAPIView.as_view(), name="items"),
    url(r'^profile/(?P<pk>[\w.@+-]+)/profile-images/$',
        UserProfileImageAPIView.as_view(), name="profile-images"),
    url(r'^profile-image/$',
        ProfileImageAPIView.as_view(), name="profile-image"),
    url(r'^profile-image/(?P<pk>\d+)/$',
        ProfileImageDetailsAPIView.as_view(), name="profile-image-details"),

     url(r'^follow/$', FollowerAddAPIView.as_view(), name='follow'),

    # user uploaded images (related to items)
    url(r'^item-image/$', ImageAPIView.as_view(), name="item-image"),
    url(r'^item-image/(?P<pk>\d+)/$',
        ImageDetailsAPIView.as_view(), name="item-image-details"),

    # user uploaded items
    url(r'^item/$', ItemAPIView.as_view(), name="item"),
    url(r'^item/(?P<pk>\d+)/$',
        ItemDetailsAPIView.as_view(), name="item-details"),
    url(r'^item/(?P<pk>\d+)/records$',
        ItemFullAPIView.as_view(), name="item-records"),

    url(r'^record/$', RecordAPIView.as_view(), name='record'),

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
}

urlpatterns = format_suffix_patterns(urlpatterns)
