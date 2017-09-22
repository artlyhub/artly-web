from django.contrib.auth import get_user_model
from rest_framework import serializers

from accounts.api.serializers import UserSerializer
from items.models import Image, Item

User = get_user_model()


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    images = serializers.HyperlinkedRelatedField(many=True,
                                                 view_name='api:image-details',
                                                 read_only=True)

    class Meta:
        model = Item
        fields = ('name',
                  'user',
                  'description',
                  'images',
                  'created',
                  'updated')


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Image
        fields = ('item',
                  'image',
                  'description',
                  'created',
                  'updated')
