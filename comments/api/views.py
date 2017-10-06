from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from comments.api.serializers import (
    CommentReplySerializer,
    ImageCommentSerializer,
    ItemCommentSerializer,
    ProfileImageCommentSerializer,
)
from comments.models import Comment, Reply
from utils.permissions import IsOwnerOrReadOnly
from utils.paginations import UserResultPagination, StandardResultPagination

User = get_user_model()


class ProfileImageCommentAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.filter(item_type='PRF').order_by('-id')
    serializer_class = ProfileImageCommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)


class ProfileImageCommentDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = ProfileImageCommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class ItemCommentAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.filter(item_type='ITM').order_by('-id')
    serializer_class = ItemCommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)


class ItemCommentDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = ItemCommentSerializer
permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class ImageCommentAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.filter(item_type='IMG').order_by('-id')
    serializer_class = ImageCommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)


class ImageCommentDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = ImageCommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class CommentReplyAPIView(generics.ListCreateAPIView):
    queryset = Reply.objects.get_queryset().order_by('-id')
    serializer_class = CommentReplySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)


class CommentReplyDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reply.objects.all()
    serializer_class = CommentReplySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
