import uuid

from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

# from records.models import Record

def scramble_uploaded_image(instance, filename):
    extension = filename.split(".")[-1]
    return "item/{}.{}".format(uuid.uuid4(), extension)


class TagManager(models.Manager):

    def search_by_tag(self, tag):
        items = Item.objects.filter(tags__contains=[tag])
        images = Image.objects.filter(tags__contains=[tag])
        return {'items': items, 'images': images}


class Item(models.Model):
    name = models.CharField(max_length=100, blank=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='items')
    description = models.TextField(blank=True)
    tags = ArrayField(models.CharField(max_length=200),
                                       null=True,
                                       blank=True,
                                       default=[''])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = TagManager()

    def __str__(self):
        return '{} - {}'.format(self.name, self.user.username)

    # @property
    # def record_history(self):
    #     record_history = []
    #     print('item/property')
    #     for record in self.records.all():
    #         history = {}
    #         history['record_number'] = record.record_number
    #         history['owner'] = record.owner.username
    #         history['purchased_price'] = record.purchased_price
    #         history['message'] = record.message
    #         history['auction_price_history'] = record.auction_price_history
    #         history['timestamp'] = record.timestamp
    #         record_history.append(history)
    #     return record_history

    @property
    def main_image(self):
        image = None
        main_image = self.images.filter(status_main=1)
        main_image_exists = main_image.exists()
        if main_image_exists:
            image = main_image.first()

        images_exist = (self.images.count() != 0)
        if not main_image_exists and images_exist:
            image = self.images.order_by('created').first()

        if image != None:
            image_url = image.image.url
            image_desc = image.description
            image_created = image.created

        if not main_image_exists and not images_exist:
            image_url = None
            image_desc = None
            image_created = None

        main_image = {
            'image': image_url,
            'description': image_desc,
            'created': image_created
        }
        return main_image


class Image(models.Model):
    item = models.ForeignKey(Item,
                             on_delete=models.CASCADE,
                             related_name='images')
    image = models.ImageField(upload_to=scramble_uploaded_image, blank=True)
    description = models.TextField(blank=True)
    tags = ArrayField(models.CharField(max_length=200),
                                       null=True,
                                       blank=True,
                                       default=[''])
    status_main = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = TagManager()

    def __str__(self):
        return '[{}]\'s image - {}'.format(self.item.name, self.item.user.username)
