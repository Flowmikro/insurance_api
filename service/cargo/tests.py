from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import CargoModel
from .serializers import CargoSerializer


class CargoListAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.cargo1 = CargoModel.objects.create(date='2022-01-01', cargo_type='Груз 1', rate=10.0, declared_value=100.0)
        self.cargo2 = CargoModel.objects.create(date='2022-01-01', cargo_type='Груз 2', rate=20.0, declared_value=200.0)
        self.cargo3 = CargoModel.objects.create(date='2022-01-02', cargo_type='Груз 3', rate=30.0, declared_value=300.0)

    def test_get_cargo_list(self):
        url = reverse('cargo_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = {
            '2022-01-01': [
                {'cargo_type': 'Груз 1', 'rate': '10.0', 'declared_value': '100.0', 'result': 1000.0},
                {'cargo_type': 'Груз 2', 'rate': '20.0', 'declared_value': '200.0', 'result': 4000.0}
            ],
            '2022-01-02': [
                {'cargo_type': 'Груз 3', 'rate': '30.0', 'declared_value': '300.0', 'result': 9000.0}
            ]
        }
        self.assertEqual(response.data, expected_data)

    def test_create_cargo(self):
        url = reverse('cargo_list')
        data = {'date': '2022-01-03', 'cargo_type': 'Груз 4', 'rate': 40.0, 'declared_value': 400.0}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CargoModel.objects.count(), 4)
        cargo = CargoModel.objects.last()
        print(cargo)
        serializer = CargoSerializer(cargo)
        self.assertEqual(response.data, serializer.data)

