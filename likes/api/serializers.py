from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ValidationError

from items.models import Image, Item
from likes.models import ImageLike, ItemLike

User = get_user_model()


class LikeItemSerializer(serializers.ModelSerializer):
    item_id = serializers.CharField(source='item', label='Item ID')

    class Meta:
        model = ItemLike
        fields = ('item_id',)
        extra_kwargs = {
            'item_id': {
                'write_only': True
            },
        }

    def validate(self, data):
        item_id = data.get('item')
        item_qs = Item.objects.filter(pk=item_id)
        if not item_qs.exists():
            raise ValidationError('존재하지 않는 작품입니다.')
        return data


class LikeImageSerializer(serializers.ModelSerializer):
    item_id = serializers.CharField(source='item', label='Image ID')

    class Meta:
        model = ImageLike
        fields = ('item_id',)
        extra_kwargs = {
            'item_id': {
                'write_only': True
            },
        }

    def validate(self, data):
        item_id = data.get('item')
        item_qs = Image.objects.filter(pk=item_id)
        if not item_qs.exists():
            raise ValidationError('존재하지 않는 이미지입니다.')
        return data
