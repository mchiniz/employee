from rest_framework import status
from rest_framework.reverse import reverse
from .models import BaseMap
from rest_framework.test import APITestCase
from model_mommy import mommy
from person.models import User


class SimpleTest(APITestCase):

    def setUp(self):
        self.base_map = mommy.make(BaseMap)
        self.user = mommy.make(User)

    def test_create_basemap_successful(self):

        data = {
            'name': 'abc',
            'url': 'https://model-mommy.readthedocs.io/en/latest/recipes.html',
            'user': self.user.pk

        }
        url = reverse("Basemap:basemap-list")
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_basemap_successful(self):
        response = self.client.get(
            reverse("Basemap:basemap-detail", kwargs={"pk": self.base_map.id}), content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_basemap_successful(self):
        response = self.client.patch(
            reverse("Basemap:basemap-detail", kwargs={'pk': self.base_map.id}),
            {'name': 'abc'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.base_map.refresh_from_db()
        self.assertEqual(self.base_map.name, 'abc')

    def test_delete_basemap_successful(self):
        self.client.force_authenticate(self.base_map)
        url = reverse("Basemap:basemap-detail", kwargs={'pk': self.base_map.id})

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
