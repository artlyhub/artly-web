from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from accounts.api.serializer import UserSearchSerializer
from items.models import Item

from utils.pagination import StandardResultsPagination

User = get_user_model()


# class UserSearchAPIView(generics.ListAPIView):
#     serializer_class = UserSearchSerializer
#     pagination_class = StandardResultsPagination
#
#     def get_queryset(self, *args, **kwargs):
#         requested_user = self.kwargs.get('username')


class ItemSearchAPIView(generics.ListAPIView):
    pass
