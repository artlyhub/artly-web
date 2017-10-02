from django.conf import settings
from django.db import models

from accounts.models import Profile
from items.models import Image, Item

ITEM_TYPES = (
    ('ITM', 'Item'),
    ('IMG', 'Image'),
)

class Comment(models.Model):
    profile = models.ForeignKey(Profile,
                                on_delete=models.CASCADE,
                                related_name='item_comments')
    item_type = models.CharField(max_length=10, choices=ITEM_TYPES)
    item = models.ForeignKey(Item,
                             on_delete=models.CASCADE,
                             related_name='comments',
                             null=True,
                             blank=True)
    image = models.ForeignKey(Image,
                              on_delete=models.CASCADE,
                              related_name='comments',
                              null=True,
                              blank=True)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.comment)


class Reply(models.Model):
    profile = models.ForeignKey(Profile,
                                on_delete=models.CASCADE,
                                related_name='comment_replies')
    cmt_parent = models.ForeignKey(Comment,
                                on_delete=models.CASCADE,
                                related_name='replies')
    reply = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.comment)
