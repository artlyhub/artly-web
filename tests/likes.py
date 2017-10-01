from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework import status

from accounts.models import Profile
from items.models import Image, Item
from likes.models import ImageLike, ItemLike

User = get_user_model()


class LikesTestCase(TestCase):
    def setUp(self):
        # create test user
        user, created = User.objects.get_or_create(username='testcase', password='test123123123')
        self.assertTrue(created, msg='user failed to create')

        # check user info
        self.user_id = user.id
        self.username = user.username
        self.profile = user.profile
        self.assertEqual(self.username, 'testcase')

        # create test item
        item, created = Item.objects.get_or_create(name='no name', user=user)
        self.assertTrue(created, msg='item failed to create')

        # check item info
        self.item_id = item.id
        self.item = item
        self.assertEqual(self.item.name, 'no name')

        # create test image
        image, created = Image.objects.get_or_create(item=self.item)
        self.assertTrue(created, msg='image failed to create')

        # check image info
        self.image_id = image.id
        self.image = image

    def test_can_like_item(self):
        # check whether user likes the item already or not
        # since the item has just been made, the user does not like the item yet
        item_liked = ItemLike.objects.does_like(self.username, self.item_id, 'item')
        self.assertFalse(item_liked, msg='user already liked the item')

        # if use does not already like the item, like the item
        ItemLike.objects.toggle_like(self.username, self.item_id, 'item')
        item_liked = ItemLike.objects.does_like(self.username, self.item_id, 'item')
        self.assertTrue(item_liked, msg='like function did not work')

        # check whether the user profile model has the itemlike instance in it
        item_exists = self.profile.item_likes.filter(item=self.item).exists()
        self.assertTrue(item_exists, msg='like function did not work')

        # try unliking the item
        ItemLike.objects.toggle_like(self.username, self.item_id, 'item')
        item_liked = ItemLike.objects.does_like(self.username, self.item_id, 'item')
        self.assertFalse(item_liked, msg='like function did not work')

    def test_can_like_image(self):
        # check whether user likes the image already or not
        # since the image has just been made, the user does not like the image yet
        image_liked = ImageLike.objects.does_like(self.username, self.image_id, 'image')
        self.assertFalse(image_liked, msg='user already liked the image')

        # if use does not already like the image, like the image
        ImageLike.objects.toggle_like(self.username, self.image_id, 'image')
        image_liked = ImageLike.objects.does_like(self.username, self.image_id, 'image')
        self.assertTrue(image_liked, msg='like function did not work')

        # check whether the user profile model has the imagelike instance in it
        image_exists = self.profile.image_likes.filter(item=self.image).exists()
        self.assertTrue(image_exists, msg='like function did not work')

        # try unliking the item
        ImageLike.objects.toggle_like(self.username, self.image_id, 'image')
        image_liked = ImageLike.objects.does_like(self.username, self.image_id, 'image')
        self.assertFalse(image_liked, msg='like function did not work')


class LikesAPITestCase(TestCase):
    def setUp(self):
        # create test user
        user, created = User.objects.get_or_create(username='testcase', password='test123123123')

        # create test item
        item, created = Item.objects.get_or_create(name='no name', user=user)
        self.item_id = item.id

        # create test image
        image, created = Image.objects.get_or_create(item=item)
        self.image_id = image.id

        self.client = APIClient()
        self.client.force_authenticate(user=user)

    def test_api_can_like_item(self):
        self.itemlike_data = {'item_id': self.item_id}
        self.response = self.client.post(
            reverse('api:item-like'),
            self.itemlike_data,
            format="json")
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_api_can_like_image(self):
        self.imagelike_data = {'item_id': self.image_id}
        self.response = self.client.post(
            reverse('api:image-like'),
            self.imagelike_data,
            format="json")
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
