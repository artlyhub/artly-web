from django.urls import reverse
from rest_framework import serializers

from items.models import Item


class ItemCardSerializer(serializers.ModelSerializer):
    main_image = serializers.SerializerMethodField()
    owner = serializers.SerializerMethodField()
    follow = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = ('id',
                  'main_image',
                  'owner',
                  'follow',
                  'name',
                  'description',
                  'created',
                  'updated',)

    def get_main_image(self, obj):
        request = self.context.get('request')
        main_image = obj.main_image
        main_image['image'] = request.build_absolute_uri(main_image['image'])
        return main_image

    def get_owner(self, obj):
        request = self.context.get('request')
        user = obj.user
        profile_image_url = user.profile.main_profile_image
        if profile_image_url != None:
            profile_image_url = request.build_absolute_uri(profile_image_url)
        profile_url = reverse('api:profile-details', args=(obj.user,))
        profile_url = request.build_absolute_uri(profile_url)
        owner = {
            'profile_image': profile_image_url,
            'username': user.username,
            'name': user.profile.name,
            'profile': profile_url
        }
        return owner

    def get_follow(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(reverse('api:follow'))
