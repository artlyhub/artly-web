from django.contrib.auth import get_user_model
from rest_framework import serializers

from groups.models import Group, GroupImage

User = get_user_model()


class GroupSerializer(serializers.ModelSerializer):
    tags = serializers.ListField(allow_null=True)
    
    class Meta:
        model = Group
        fields = ('id',
                  'name',
                  'admin',
                  'staff',
                  'member',
                  'description',
                  'tags',
                  'created',
                  'updated',)
        read_only_fields = ('admin',
                            'created',
                            'updated',)


class GroupImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupImage
        fields = ('id',
                  'group',
                  'image',
                  'description',
                  'status_main',
                  'created',
                  'update',)
