from django.test import TestCase
from api import models
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory

#Institution View


def create_city(name):
    return models.City.objects.create(name=name)


def create_category(name):
    return models.Category.objects.create(name=name)


def create_institution(name):
    new_city = create_city('Porto')
    new_category = create_category('Institution')

    new_institution = models.Institution.objects.create(
        name=name,
        abbr="",
        email="",
        phone="913371337",
        fax="913371337",
        address="",
        postal_code="1234-123",
        city=new_city.id,
        category=new_category.id,
    )
    return new_institution


class InstitutionViewTests(TestCase):
    def test_index_view_empty(self):
        url = reverse('institution-list')
        data = []
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, data)

    def test_index_view_create(self):
        my_city = create_city('Porto')
        my_category = create_category('Institution')

        url = reverse('institution-list')
        data = {
                    "name": "Universidade do Porto",
                    "abbr": "UP",
                    "email": "email@email.com",
                    "phone": "913371337",
                    "fax": "913371337",
                    "address": "Rua Dr. Roberto Frias, s/n",
                    "postal_code": "1234-123",
                    "city": my_city.id,
                    "category": my_category.id,
                }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_index_view_create_and_view(self):
        my_city = create_city('Porto')
        my_category = create_category('Institution')

        post_data = {
            "name": "Universidade do Porto",
            "abbr": "UP",
            "email": "email@email.com",
            "phone": "913371337",
            "fax": "913371337",
            "address": "Rua Dr. Roberto Frias, s/n",
            "postal_code": "1234-123",
            "city": my_city.id,
            "category": my_category.id,
        }

        url = reverse('institution-list')

        self.client.post(url, post_data)

        response = self.client.get(url)

        get_data = [{
            "id": 1,
            "name": "Universidade do Porto",
            "abbr": "UP",
            "category": "Institution"
        }]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, get_data)

    def test_index_view_create_invalid_abbr(self):
        my_city = create_city('Porto')
        my_category = create_category('Institution')

        url = reverse('institution-list')
        data = {
                    "name": "Universidade do Porto",
                    "abbr": "123456789012345678901234567890123456789012345678901",
                    "email": "email@email.com",
                    "phone": "913371337",
                    "fax": "913371337",
                    "address": "Rua Dr. Roberto Frias, s/n",
                    "postal_code": "1234-123",
                    "city": my_city.id,
                    "category": my_category.id,
                }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_index_view_create_invalid_phonenumber(self):
        my_city = create_city('Porto')
        my_category = create_category('Institution')

        url = reverse('institution-list')
        data = {
                    "name": "Universidade do Porto",
                    "abbr": "UP",
                    "email": "email@email.com",
                    "phone": "9133713370",
                    "fax": "913371337",
                    "address": "Rua Dr. Roberto Frias, s/n",
                    "postal_code": "1234-123",
                    "city": my_city.id,
                    "category": my_category.id,
                }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



