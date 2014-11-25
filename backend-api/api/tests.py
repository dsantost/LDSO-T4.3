from django.test import TestCase
from api import models
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory

#########################################################################
# Institution View
#########################################################################


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


def create_institution_json(name):
    new_city = create_city('Porto')
    new_category = create_category('Institution')

    new_institution = {
        "name": name,
        "abbr": "UP",
        "email": "email@email.com",
        "phone": "913371337",
        "fax": "913371337",
        "address": "Rua Dr. Roberto Frias, s/n",
        "postal_code": "1234-123",
        "city": new_city.id,
        "category": new_category.id,
    }
    return new_institution


class InstitutionViewTests(TestCase):

    def test_index_view_empty(self):
        url = reverse('institution-list')
        data = []
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, data)


    def test_index_view_create(self):
        url = reverse('institution-list')
        data = create_institution_json("Universidade do Porto")
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_index_view_create_and_view(self):
        url = reverse('institution-list')
        post_data = create_institution_json("Universidade do Porto")
        self.client.post(url, post_data)

        #posted new institution, should now look for it on the list of all institutions
        response = self.client.get(url)

        get_data = [{
            "id": 1,
            "name": "Universidade do Porto",
            "abbr": "UP",
            "category": "Institution"
        }]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, get_data)


    def test_index_view_create_invalid_abbr_length(self):
        url = reverse('institution-list')
        data = create_institution_json("Universidade do Porto")
        data["abbr"] = "123456789012345678901234567890123456789012345678901"
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_index_view_create_invalid_phone_length(self):
        url = reverse('institution-list')
        data = create_institution_json("Universidade do Porto")
        data["phone"] = "12345678901234"
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_index_view_create_invalid_fax_length(self):
        url = reverse('institution-list')
        data = create_institution_json("Universidade do Porto")
        data["fax"] = "12345678901234"
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_index_view_create_invalid_postal_code_length(self):
        url = reverse('institution-list')
        data = create_institution_json("Universidade do Porto")
        data["postal_code"] = "123456789"
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_index_view_create_invalid_page_color_length(self):
        url = reverse('institution-list')
        data = create_institution_json("Universidade do Porto")
        data["page_color"] = "123456789"
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_index_view_create_invalid_phone_regex(self):
        url = reverse('institution-list')
        data = create_institution_json("Universidade do Porto")
        data["phone"] = "9133713370"
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_index_view_create_invalid_fax_regex(self):
        url = reverse('institution-list')
        data = create_institution_json("Universidade do Porto")
        data["fax"] = "9133713370"
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_index_view_create_invalid_postal_code_regex(self):
        url = reverse('institution-list')
        data = create_institution_json("Universidade do Porto")
        data["postal_code"] = "1234567"
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_view_create_unique_name(self):
        url = reverse('institution-list')
        data = create_institution_json("Universidade do Porto")
        dup_data = create_institution_json("Universidade do Porto")
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        #posted new institution, should now try creating a duplicate one
        response = self.client.post(url, dup_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_view_create_default_page_color(self):
        url = reverse('institution-list')
        data = create_institution_json("Universidade do Porto")
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        #posted new institution, should now get created object
        url = reverse('institution-detail', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.data["page_color"], "ffffff")


    def test_view_create_invalid_city_key(self):
        url = reverse('institution-list')
        data = create_institution_json("Universidade do Porto")
        data["city"] = "2"
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_view_create_invalid_category_key(self):
        url = reverse('institution-list')
        data = create_institution_json("Universidade do Porto")
        data["city"] = "2"
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

#########################################################################
# Student View
#########################################################################


def create_user(name):
    return models.User.objects.create(username=name, password="pass")


def create_student_json(name):
    new_user = create_user(name)

    new_student = {
        'user': new_user.id,
        "name": name,
    }
    return new_student


class StudentViewTests(TestCase):

    def test_index_view_empty(self):
        url = reverse('student-list')
        data = []
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, data)


    def test_index_view_create(self):
        url = reverse('student-list')
        data = create_student_json("Vasco")
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_index_view_create_and_view(self):
        url = reverse('student-list')
        post_data = create_student_json("Hugo")
        self.client.post(url, post_data)

        #posted new institution, should now look for it on the list of all institutions
        response = self.client.get(url)

        get_data = [{
            "id": 1,
            "name": "Hugo",
            "enrollments": []
        }]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, get_data)
