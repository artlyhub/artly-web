from django.contrib.auth import get_user_model
from rest_framework import serializers

from items.models import Image, Item

User = get_user_model()


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    tags = serializers.ListField(allow_null=True)

    class Meta:
        model = Image
        fields = ('id',
                  'item',
                  'image',
                  'description',
                  'tags',
                  'status_main',
                  'created',
                  'updated',)


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    tags = serializers.ListField(allow_null=True)
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = ('id',
                  'name',
                  'user',
                  'description',
                  'tags',
                  'images',
                  'created',
                  'updated',)
