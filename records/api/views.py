from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework.views import APIView

from records.api.serializers import RecordSerializer
from records.models import Record

User = get_user_model()


class RecordAPIView(generics.ListCreateAPIView):
    queryset = Record.objects.get_queryset().order_by('timestamp')
    serializer_class = RecordSerializer
