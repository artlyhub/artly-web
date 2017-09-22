import uuid

from django.conf import settings
from django.db import models

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


# models that depend on any of the above models
class Image(models.Model):
    item = models.ForeignKey(Item,
                             on_delete=models.CASCADE,
                             related_name='images')
    image = models.ImageField(upload_to=scramble_uploaded_image)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '[{}]\'s image - {}'.format(self.item.name, self.item.user.username)
