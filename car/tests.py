from rest_framework import status
from rest_framework.reverse import reverse
from .models import Car
from rest_framework.test import APITestCase
from model_mommy import mommy


class SimpleTest(APITestCase):

    def setUp(self):
        self.new_car = mommy.make(Car)

    def test_create_car_successful(self):
        data = {
            'name': 'benz',
            'code': '7',
            'color': 'red',
            'plaque': 'sdfasdf'

        }
        url = reverse("Car:car-list")
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_car_successful(self):
        response = self.client.get(
            reverse("Car:car-detail", kwargs={"pk": self.new_car.id}), content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_car_successful(self):
        # user = User.objects.create(username="nazi12", password='abc', first_name='sajad', last_name='sdfasdf')

        response = self.client.patch(
            reverse("Car:car-detail", kwargs={"pk": self.new_car.id}),
            data={"name": "abc"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.new_car.refresh_from_db()
        self.assertEqual(self.new_car.name, 'abc')

    def test_patch_car_successful(self):
        # user = User.objects.create(username="nazi12", password='abc', first_name='sajad', last_name='sdfasdf')

        response = self.client.patch(
            reverse("Car:car-detail", kwargs={'pk': self.new_car.id}),
            {'name': 'abc'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.new_car.refresh_from_db()
        self.assertEqual(self.new_car.name, 'abc')

    def test_delete_car_successful(self):
        # user = User.objects.create(username="nazi12", password='abc', first_name='sajad', last_name='sdfasdf')

        self.client.force_authenticate(self.new_car)
        url = reverse("Car:car-detail", kwargs={'pk': self.new_car.id})

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
