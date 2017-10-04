from django.urls import reverse
from rest_framework import serializers

from accounts.models import Profile
from items.models import Item
from likes.models import ItemLike


class ItemCardSerializer(serializers.ModelSerializer):
    main_image = serializers.SerializerMethodField()
    owner = serializers.SerializerMethodField()
    following = serializers.SerializerMethodField()
    follow = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()
    liked = serializers.SerializerMethodField()
    like = serializers.SerializerMethodField()
    detail = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = ('id',
                  'main_image',
                  'owner',
                  'following',
                  'follow',
                  'likes',
                  'liked',
                  'like',
                  'name',
                  'description',
                  'detail',
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
        profile_image_url = user.profile.profile_image
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

    def get_following(self, obj):
        request = self.context.get('request')
        req_user = request.user.username
        owner = obj.user
        return Profile.objects.is_following(req_user, owner)

    def get_follow(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(reverse('api:follow'))

    def get_likes(self, obj):
        return obj.liked.count()

    def get_liked(self, obj):
        request = self.context.get('request')
        req_user = request.user.username
        item_id = obj.id
        return ItemLike.objects.does_like(req_user, item_id, 'item')

    def get_like(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(reverse('api:item-like'))

    def get_detail(self, obj):
        request = self.context.get('request')
        item_details_url = reverse('api:item-details', args=(obj.id,))
        return request.build_absolute_uri(item_details_url)
