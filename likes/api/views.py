from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from accounts.models import ProfileImage
from comments.models import Comment, Reply
from groups.models import Group
from items.models import Image, Item
from likes.models import (
    CommentLike,
    GroupLike,
    ImageLike,
    ItemLike,
    ProfileImageLike,
    ReplyLike,
)
from likes.api.serializers import (
    LikeCommentSerializer,
    LikeGroupSerializer,
    LikeImageSerializer,
    LikeItemSerializer,
    LikeProfileImageSerializer,
    LikeReplySerializer,
)

from utils.permissions import IsOwnerOrReadOnly
from utils.paginations import UserResultPagination, StandardResultPagination

User = get_user_model()


class LikeProfileImageAPIView(APIView):
    serializer_class = LikeProfileImageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            data = request.data
            serializer = LikeProfileImageSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                item_id = serializer.data['item_id']
                to_toggle_item = ProfileImage.objects.filter(pk=item_id).first()
                liked = ProfileImageLike.objects.toggle_like(request.user.username, to_toggle_item.id, 'item')
                if liked:
                    return Response({'status': 'liked'}, status=HTTP_200_OK)
                else:
                    return Response({'status': 'unliked'}, status=HTTP_200_OK)
            return Response(serializers.errors, status=HTTP_400_BAD_REQUEST)


class LikeItemAPIView(APIView):
    serializer_class = LikeItemSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            data = request.data
            serializer = LikeItemSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                item_id = serializer.data['item_id']
                to_toggle_item = Item.objects.filter(pk=item_id).first()
                liked = ItemLike.objects.toggle_like(request.user.username, to_toggle_item.id, 'item')
                if liked:
                    return Response({'status': 'liked'}, status=HTTP_200_OK)
                else:
                    return Response({'status': 'unliked'}, status=HTTP_200_OK)
            return Response(serializers.errors, status=HTTP_400_BAD_REQUEST)


class LikeImageAPIView(APIView):
    serializer_class = LikeImageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            data = request.data
            serializer = LikeImageSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                item_id = serializer.data['item_id']
                to_toggle_item = Image.objects.filter(pk=item_id).first()
                liked = ImageLike.objects.toggle_like(request.user.username, to_toggle_item.id, 'image')
                if liked:
                    return Response({'status': 'liked'}, status=HTTP_200_OK)
                else:
                    return Response({'status': 'unliked'}, status=HTTP_200_OK)
            return Response(serializers.errors, status=HTTP_400_BAD_REQUEST)


class LikeGroupAPIView(APIView):
    serializer_class = LikeGroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            data = request.data
            serializer = LikeGroupSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                item_id = serializer.data['item_id']
                to_toggle_item = Group.objects.filter(pk=item_id).first()
                liked = GroupLike.objects.toggle_like(request.user.username, to_toggle_item.id, 'item')
                if liked:
                    return Response({'status': 'liked'}, status=HTTP_200_OK)
                else:
                    return Response({'status': 'unliked'}, status=HTTP_200_OK)
            return Response(serializers.errors, status=HTTP_400_BAD_REQUEST)


class LikeCommentAPIView(APIView):
    serializer_class = LikeCommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            data = request.data
            serializer = LikeCommentSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                item_id = serializer.data['item_id']
                to_toggle_item = Comment.objects.filter(pk=item_id).first()
                liked = CommentLike.objects.toggle_like(request.user.username, to_toggle_item.id, 'comment')
                if liked:
                    return Response({'status': 'liked'}, status=HTTP_200_OK)
                else:
                    return Response({'status': 'unliked'}, status=HTTP_200_OK)
            return Response(serializers.errors, status=HTTP_400_BAD_REQUEST)


class LikeReplyAPIView(APIView):
    serializer_class = LikeReplySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            data = request.data
            serializer = LikeReplySerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                item_id = serializer.data['item_id']
                to_toggle_item = Reply.objects.filter(pk=item_id).first()
                liked = ReplyLike.objects.toggle_like(request.user.username, to_toggle_item.id, 'reply')
                if liked:
                    return Response({'status': 'liked'}, status=HTTP_200_OK)
                else:
                    return Response({'status': 'unliked'}, status=HTTP_200_OK)
            return Response(serializers.errors, status=HTTP_400_BAD_REQUEST)
