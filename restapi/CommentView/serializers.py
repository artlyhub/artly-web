from django.urls import reverse
from rest_framework import serializers

from accounts.models import Profile
from comments.models import Comment, Reply
from items.models import Item
from likes.models import CommentLike, ReplyLike


class _ReplySerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()
    liked = serializers.SerializerMethodField()

    class Meta:
        model = Reply
        fields = ('id',
                  'profile',
                  'reply',
                  'likes',
                  'liked',
                  'created',
                  'updated',)

    def get_likes(self, obj):
        return obj.liked.count()

    def get_liked(self, obj):
        request = self.context.get('request')
        req_user = request.user.username
        reply_id = obj.id
        return ReplyLike.objects.does_like(req_user, reply_id, 'reply')


class CommentSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()
    liked = serializers.SerializerMethodField()
    replies = _ReplySerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ('id',
                  'item_type',
                  'profile',
                  'comment',
                  'likes',
                  'liked',
                  'replies',
                  'created',
                  'updated',)

    def get_likes(self, obj):
        return obj.liked.count()

    def get_liked(self, obj):
        request = self.context.get('request')
        req_user = request.user.username
        comment_id = obj.id
        return CommentLike.objects.does_like(req_user, comment_id, 'comment')
