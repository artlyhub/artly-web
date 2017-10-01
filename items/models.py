import uuid

from django.conf import settings
from django.db import models

# from records.models import Record

def scramble_uploaded_image(instance, filename):
    extension = filename.split(".")[-1]
    return "item/{}.{}".format(uuid.uuid4(), extension)


class Item(models.Model):
    name = models.CharField(max_length=100, blank=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='items')
    description = description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.name, self.user.username)

    @property
    def record_history(self):
        record_history = []
        print('item/property')
        for record in self.records.all():
            history = {}
            history['record_number'] = record.record_number
            history['owner'] = record.owner.username
            history['purchased_price'] = record.purchased_price
            history['message'] = record.message
            history['auction_price_history'] = record.auction_price_history
            history['timestamp'] = record.timestamp
            record_history.append(history)
        return record_history

    @property
    def main_image(self):
        image = self.images.get(status_main=1)
        main_image = {
            'image': image.image.url,
            'description': image.description,
            'created': image.created
        }
        return main_image


class Image(models.Model):
    item = models.ForeignKey(Item,
                             on_delete=models.CASCADE,
                             related_name='images')
    image = models.ImageField(upload_to=scramble_uploaded_image, blank=True)
    description = models.TextField(blank=True)
    status_main = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '[{}]\'s image - {}'.format(self.item.name, self.item.user.username)
