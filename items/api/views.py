from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_403_FORBIDDEN,)
from rest_framework.views import APIView

from items.api.serializers import ImageSerializer, ItemSerializer
from items.models import Image, Item
from utils.permissions import IsOwnerOrReadOnly
from utils.paginations import UserResultPagination, StandardResultPagination

User = get_user_model()


## Issue: None
class ItemAPIView(generics.ListCreateAPIView):
    queryset = Item.objects.get_queryset().order_by('id')
    serializer_class = ItemSerializer
    pagination_class = StandardResultPagination
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


## Issue: None
class ItemDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)


## Issue: None
class ImageAPIView(generics.ListCreateAPIView):
    queryset = Image.objects.get_queryset().order_by('id')
    serializer_class = ImageSerializer
    pagination_class = StandardResultPagination
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = ImageSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            item_id = serializer.data['item']
            item = Item.objects.get(id=item_id)
            owner = item.user.username
            if owner != request.user.username:
                return Response({'status': '유저의 작품글이 아닙니다. 수정할 수 없습니다.'}, status=HTTP_403_FORBIDDEN)
            else:
                return self.create(request, *args, **kwargs)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


## Issue: None
class ImageDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
