import uuid

from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.db import models

def scramble_uploaded_image(instance, filename):
    extension = filename.split(".")[-1]
    return "group/{}.{}".format(uuid.uuid4(), extension)


class Group(models.Model):
    name = models.CharField(max_length=100, blank=False)
    admin = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='my_groups')
    staff = models.ManyToManyField(settings.AUTH_USER_MODEL,
                             related_name='as_staff_groups')
    member = models.ManyToManyField(settings.AUTH_USER_MODEL,
                             related_name='as_member_groups')
    description = models.TextField()
    tags = ArrayField(models.CharField(max_length=200),
                                       null=True,
                                       blank=True,
                                       default=[''])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}\'s group - {}'.format(self.admin.username, self.name)


class GroupImage(models.Model):
    group = models.ForeignKey(Group,
                            on_delete=models.CASCADE,
                            related_name='group_images')
    image = models.ImageField(upload_to=scramble_uploaded_image)
    description = models.TextField()
    status_main = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} ({})'.format(self.group.name, self.id)
