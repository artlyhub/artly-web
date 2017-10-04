from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework import status

from accounts.models import Profile
from items.models import Image, Item
from likes.models import ImageLike, ItemLike

User = get_user_model()


class AccountsTestCase(TestCase):
    def setUp(self):
        # create test user
        user, created = User.objects.get_or_create(username='testcase', password='test123123123')
        self.assertTrue(created, msg='user failed to create')

        # test whether profile created or not
        user_id = user.id
        self.assertEqual(user.profile.user, user, msg='profile failed to create')


class AccountsAPITestCase(TestCase):
    # testing CRUD of accounts api

    def setUp(self):
        self.client = APIClient()

        # create new user using /api/user/ with post request
        self.user = {'username': 'testcase',
                'email': 'test@gmail.com',
                'password': 'test123123123'}
        response = self.client.post(
            '/api/user/',
            self.user,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # check created user specs
        self.assertEqual(User.objects.get(pk=1).username, self.user['username'])
        self.assertEqual(User.objects.get(pk=1).email, self.user['email'])

    def test_api_can_retrieve_user(self):
        # test whether retrieve works
        response = self.client.get('/api/user/{}/'.format(self.user['username']))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user['username'])

    def test_api_can_update_user_data(self):
        # test whether put available / before authentication
        new_email = {'email': 'test1@gmail.com'}
        response = self.client.put('/api/user/{}'.format(self.user['username']),
                                   new_email,
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)

    # def test_user_api_creates_profile(self):
