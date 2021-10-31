# from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from .models import User
from rest_framework.test import APITestCase
from model_mommy import mommy


class SimpleTest(APITestCase):

    def setUp(self):
        self.user = mommy.make(User)

    def test_create_user_successful(self):
        data = {
            'username': 'hassan',
            'password': '12334',
            'first_name': 'ali',
            'last_name': 'sdfasdf'
        }
        url = reverse("person:user-list")
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_user_successful(self):
        response = self.client.get(
            reverse("person:user-detail", kwargs={"pk": self.user.id}), content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_user_successful(self):
        response = self.client.patch(
            reverse("person:user-detail", kwargs={'pk': self.user.id}),
            {'first_name': 'abc'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'abc')

    def test_delete_user_successful(self):
        # user = User.objects.create(username="nazi12", password='abc', first_name='sajad', last_name='sdfasdf')

        self.client.force_authenticate(user=self.user)
        url = reverse("person:user-detail", kwargs={'pk': self.user.id})

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
