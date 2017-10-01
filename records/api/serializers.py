from django.contrib.auth import get_user_model
from django.urls import reverse, reverse_lazy
from rest_framework import serializers
from rest_framework.serializers import ValidationError

from items.api.serializers import ImageSerializer, ItemSerializer
from items.models import Item
from records.models import Record

User = get_user_model()


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ('item',
                  'record_number',
                  'timestamp',
                  'artist',
                  'purchased_price',
                  'owner',
                  'message',
                  'for_sale',
                  'sale_method',
                  'sale_price',
                  'auction_price_history',
                  'private_info',
                  'artly_possession',
                  'previous_hash',
                  'current_hash',)


class ItemFullSerializer(serializers.ModelSerializer):
    user_url = serializers.SerializerMethodField()
    images = ImageSerializer(many=True, read_only=True)
    records = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = ('id',
                  'name',
                  'description',
                  'user_url',
                  'images',
                  'records',)

    def get_user_url(self, obj):
        request = self.context.get('request')
        url = reverse('api:user-details', args=(obj.user.username,))
        return request.build_absolute_uri(url)

    def get_records(self, obj):
        return obj.record_history
