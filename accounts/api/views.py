from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from accounts.api.serializers import (
    FollowerAddSerializer,
    FollowerSerializer,
    ProfileImageSerializer,
    ProfileSerializer,
    # UserItemSerializer,
    UserLoginSerializer,
    UserSerializer,
)
# from items.api.serializers import ImageSerializer, ItemSerializer
from accounts.models import Profile, ProfileImage
# from items.models import Image, Item

User = get_user_model()


class UserAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'


class UserLoginAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.data['username']
            user = User.objects.filter(username=username).first()
            token = Token.objects.filter(user=user).first().key
            return Response({'token': token}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class ProfileAPIView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProfileDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileImageAPIView(generics.ListCreateAPIView):
    queryset = ProfileImage.objects.all()
    serializer_class = ProfileImageSerializer


class ProfileImageDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProfileImage.objects.all()
    serializer_class = ProfileImageSerializer


class FollowerAPIView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = FollowerSerializer


class FollowerAddAPIView(APIView):
    serializer_class = FollowerAddSerializer

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            data = request.data
            serializer = FollowerAddSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                follow = serializer.data['follow']
                to_toggle_user = User.objects.all().filter(username=follow).first()
                following = Profile.objects.toggle_follow(request.user, to_toggle_user)
                if following:
                    return Response({'status': 'followed'}, status=HTTP_200_OK)
                else:
                    return Response({'status': 'unfollowed'}, status=HTTP_200_OK)
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
