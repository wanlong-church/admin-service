from datetime import date, time

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Service, ServiceGroup, ServiceNote, ServiceType


class TestConfig:
    NOTE = "pray together at 9:50"
    GROUP = "pastoral"
    SERVICE_TYPE = "sermon"
    START_TIME = time(9, 0)
    END_TIME = time(11, 30)


class ModelTestCase(TestCase):
    def setUp(self):
        self.service_note = ServiceNote.objects.create(content=TestConfig.NOTE)
        self.service_group = ServiceGroup.objects.create(name=TestConfig.GROUP)
        self.service_type = ServiceType.objects.create(
            name=TestConfig.SERVICE_TYPE,
            start_time=TestConfig.START_TIME,
            end_time=TestConfig.END_TIME,
            service_group=self.service_group,
        )
        self.service_type.notes.add(self.service_note)
        self.service = Service.objects.create(
            service_type=self.service_type, date=date.today()
        )

    def test_service_note_str(self):
        self.assertEqual(str(self.service_note), f"Note {self.service_note.id}")

    def test_service_type_str(self):
        self.assertEqual(str(self.service_type), TestConfig.SERVICE_TYPE)

    def test_service_group_str(self):
        self.assertEqual(str(self.service_group), TestConfig.GROUP)

    def test_service_str(self):
        expected = f"Service {self.service.id} - {TestConfig.SERVICE_TYPE}"
        self.assertEqual(str(self.service), expected)

    def test_service_type_service_group(self):
        self.assertEqual(self.service_type.service_group, self.service_group)

    def test_service_type_notes(self):
        self.assertIn(self.service_note, self.service_type.notes.all())


class ServiceAPITest(APITestCase):
    def setUp(self):
        self.service_group = ServiceGroup.objects.create(name=TestConfig.GROUP)
        self.service_type = ServiceType.objects.create(
            name=TestConfig.SERVICE_TYPE,
            start_time=TestConfig.START_TIME,
            end_time=TestConfig.END_TIME,
            service_group=self.service_group,
        )

    def test_list_service_types(self):
        url = reverse("service:type-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)

    def test_create_service_type(self):
        url = reverse("service:type-list")
        data = {
            "name": TestConfig.SERVICE_TYPE,
            "start_time": TestConfig.START_TIME.strftime("%H:%M:%S"),
            "end_time": TestConfig.END_TIME.strftime("%H:%M:%S"),
            "service_group": self.service_group.id,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ServiceType.objects.count(), 2)

    def test_list_service_groups(self):
        url = reverse("service:group-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)

    def test_create_service(self):
        url = reverse("service:list")
        data = {
            "service_type": self.service_type.id,
            "date": date.today().strftime("%Y-%m-%d"),
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Service.objects.count(), 1)
