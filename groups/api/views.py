from django.contrib.auth import get_user_model
from rest_framework import generics, permissions

from groups.api.serializers import GroupSerializer, GroupImageSerializer
from groups.models import Group, GroupImage
from utils.paginations import UserResultPagination, StandardResultPagination
from utils.permissions import IsOwnerOrReadOnly

User = get_user_model()


class GroupAPIView(generics.ListCreateAPIView):
    queryset = Group.objects.get_queryset().order_by('-id')
    serializer_class = GroupSerializer
    pagination_class = UserResultPagination
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(admin=self.request.user)


class GroupDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)


class GroupImageAPIView(generics.ListCreateAPIView):
    queryset = GroupImage.objects.get_queryset().order_by('-id')
    serializer_class = GroupImageSerializer
    pagination_class = StandardResultPagination


class GroupImageDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GroupImage.objects.all()
    serializer_class = GroupImageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
