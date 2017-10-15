from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ValidationError

from accounts.models import Profile, ProfileImage
from comments.models import Comment, Reply
from groups.models import Group
from items.models import Image, Item

User = get_user_model()


class ProfileImageCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id',
                  'profile',
                  'item_type',
                  'profile_image',
                  'comment',
                  'created',
                  'updated',)
        read_only_fields = ('profile',
                            'item_type',
                            'created',
                            'updated',)

    def create(self, validated_data):
        profile = validated_data['profile']
        item_type = 'PRF'
        profile_image = validated_data['profile_image']
        comment = validated_data['comment']
        comment_obj = Comment(
            profile=profile,
            item_type=item_type,
            profile_image=profile_image,
            comment=comment
        )
        comment_obj.save()
        return comment_obj


class ItemCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id',
                  'profile',
                  'item_type',
                  'item',
                  'comment',
                  'created',
                  'updated',)
        read_only_fields = ('profile',
                            'item_type',
                            'created',
                            'updated',)

    def create(self, validated_data):
        profile = validated_data['profile']
        item_type = 'ITM'
        item = validated_data['item']
        comment = validated_data['comment']
        comment_obj = Comment(
            profile=profile,
            item_type=item_type,
            item=item,
            comment=comment
        )
        comment_obj.save()
        return comment_obj


class ImageCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id',
                  'profile',
                  'item_type',
                  'image',
                  'comment',
                  'created',
                  'updated',)
        read_only_fields = ('profile',
                            'item_type',
                            'created',
                            'updated',)

    def create(self, validated_data):
        profile = validated_data['profile']
        item_type = 'IMG'
        image = validated_data['image']
        comment = validated_data['comment']
        comment_obj = Comment(
            profile=profile,
            item_type=item_type,
            image=image,
            comment=comment
        )
        comment_obj.save()
        return comment_obj


class GroupCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id',
                  'profile',
                  'item_type',
                  'group',
                  'comment',
                  'created',
                  'updated',)
        read_only_fields = ('profile',
                            'item_type',
                            'created',
                            'updated',)

    def create(self, validated_data):
        profile = validated_data['profile']
        item_type = 'GRP'
        group = validated_data['group']
        comment = validated_data['comment']
        comment_obj = Comment(
            profile=profile,
            item_type=item_type,
            group=group,
            comment=comment
        )
        comment_obj.save()
        return comment_obj


class CommentReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ('id',
                  'profile',
                  'cmt_parent',
                  'reply',
                  'created',
                  'updated',)
        read_only_fields = ('profile',
                            'created',
                            'updated',)
