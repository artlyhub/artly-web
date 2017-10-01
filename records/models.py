from django.conf import settings
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from items.models import Item

SALE_METHOD = (
    ('Sale', 'Regular Sale'),
    ('Fund', 'Crowd Art Fund'),
    ('Auction', 'Auction'),
)


class RecordManager(models.Manager):
    pass

class Record(models.Model):
    record_number = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    artist = models.CharField(max_length=50)
    item = models.ForeignKey(Item,
                             on_delete=models.CASCADE,
                             related_name='records')
    purchased_price = models.BigIntegerField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name='owned_items')
    message = models.TextField(default='')
    for_sale = models.BooleanField(default=1)
    sale_method = models.CharField(max_length=7,
                                   choices=SALE_METHOD,
                                   default='Sale')
    sale_price = models.BigIntegerField()
    auction_price_history = JSONField(default='{}')
    private_info = models.BooleanField(default=0)
    artly_possession = models.BooleanField(default=0)
    previous_hash = models.CharField(max_length=64, default='')
    current_hash = models.CharField(max_length=64, default='')

    objects = RecordManager()

    def __str__(self):
        return '{}'.format(self.current_hash)
