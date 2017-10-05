from django.conf import settings
from django.db import models

from accounts.models import Profile, ProfileImage
from comments.models import Comment, Reply
from items.models import Image, Item


class LikeManager(models.Manager):
    # manages like action and like status for: Item, Image

    def does_like(self, username, item_id, item_type):
        # item_type: "item", "image"
        profile = Profile.objects.get(user=username)
        qs = {
            'profile_image': profile.profile_image_likes,
            'item': profile.item_likes,
            'image': profile.image_likes,
            'comment': profile.comment_likes,
            'reply': profile.reply_likes
        }
        if qs[item_type].filter(item=item_id).exists():
            return True
        return False

    def toggle_like(self, username, item_id, item_type):
        profile = Profile.objects.get(user=username)
        model = {
            'profile_image': ProfileImage,
            'item': Item,
            'image': Image,
            'comment': Comment,
            'reply': Reply
        }
        model_like = {
            'profile_image': ProfileImageLike,
            'item': ItemLike,
            'image': ImageLike,
            'comment': CommentLike,
            'reply': ReplyLike
        }
        qs = {
            'profile_image': profile.profile_image_likes,
            'item': profile.item_likes,
            'image': profile.image_likes,
            'comment': profile.comment_likes,
            'reply': profile.reply_likes
        }
        item = model[item_type].objects.get(pk=item_id)
        if model_like[item_type].objects.does_like(username, item_id, item_type):
            qs[item_type].filter(item=item).delete()
            item.liked.filter(profile=profile).delete()
            liked = False
        else:
            itemlike = model_like[item_type](profile=profile, item=item)
            itemlike.save()
            liked = True
        return liked


class ProfileImageLike(models.Model):
    profile = models.ForeignKey(Profile,
                                on_delete=models.CASCADE,
                                related_name='profile_image_likes')
    item = models.ForeignKey(ProfileImage,
                             on_delete=models.CASCADE,
                             related_name='liked',
                             null=True,
                             blank=True)

    objects = LikeManager()

    def __str__(self):
        return '{} likes {}'.format(self.profile.user.username, self.item)


class ItemLike(models.Model):
    profile = models.ForeignKey(Profile,
                                on_delete=models.CASCADE,
                                related_name='item_likes')
    item = models.ForeignKey(Item,
                             on_delete=models.CASCADE,
                             related_name='liked',
                             null=True,
                             blank=True)

    objects = LikeManager()

    def __str__(self):
        return '{} likes {}'.format(self.profile.user.username, self.item)


class ImageLike(models.Model):
    profile = models.ForeignKey(Profile,
                                on_delete=models.CASCADE,
                                related_name='image_likes')
    item = models.ForeignKey(Image,
                              on_delete=models.CASCADE,
                              related_name='liked',
                              null=True,
                              blank=True)

    objects = LikeManager()

    def __str__(self):
        return '{} likes {}'.format(self.profile.user.username, self.item)


class CommentLike(models.Model):
    profile = models.ForeignKey(Profile,
                                on_delete=models.CASCADE,
                                related_name='comment_likes')
    item = models.ForeignKey(Comment,
                             on_delete=models.CASCADE,
                             related_name='liked',
                             null=True,
                             blank=True)

    objects = LikeManager()

    def __str__(self):
        return '{} likes {}'.format(self.profile.user.username, self.item)


class ReplyLike(models.Model):
    profile = models.ForeignKey(Profile,
                                on_delete=models.CASCADE,
                                related_name='reply_likes')
    item = models.ForeignKey(Reply,
                             on_delete=models.CASCADE,
                             related_name='liked',
                             null=True,
                             blank=True)

    objects = LikeManager()

    def __str__(self):
        return '{} likes {}'.format(self.profile.user.username, self.item)
