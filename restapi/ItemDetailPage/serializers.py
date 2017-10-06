from django.urls import reverse
from rest_framework import serializers

from accounts.models import Profile
from items.models import Item
from likes.models import ItemLike


class ItemDetailPageSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    owner = serializers.SerializerMethodField()
    following = serializers.SerializerMethodField()
    follow = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()
    liked = serializers.SerializerMethodField()
    like = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = ('id',
                  'images',
                  'owner',
                  'following',
                  'follow',
                  'likes',
                  'liked',
                  'like',
                  'name',
                  'description',
                  'tags',
                  'created',
                  'updated',)

    def get_images(self, obj):
        request = self.context.get('request')

        main_image = obj.images.filter(status_main=1)
        main_image_exists = main_image.exists()
        images_exist_other_than_main_image = (obj.images.exclude(status_main=1).count() != 0)

        if main_image_exists:
            main_image = main_image.first()
            total_images = [main_image]
        else:
            total_images = []

        if images_exist_other_than_main_image:
            images_other_than_main_image = list(obj.images.exclude(status_main=1).order_by('created'))

        images = []
        total_images += images_other_than_main_image

        for image_obj in total_images:
            image_url = image_obj.image.url
            image = {
                'id': image_obj.id,
                'status_main': image_obj.status_main,
                'image': request.build_absolute_uri(image_url),
                'description': image_obj.description,
                'created': image_obj.created,
                'updated': image_obj.updated
            }
            images.append(image)
        return images

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
