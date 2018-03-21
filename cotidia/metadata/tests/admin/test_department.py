from django.test import TestCase, Client
from django.urls import reverse

from cotidia.account import fixtures
from cotidia.metadata.models import Department
from cotidia.metadata.factory import DepartmentFactory


class DepartmentAdminTests(TestCase):

    @fixtures.superuser
    def setUp(self):

        # Create a default object, to use with update, retrieve, list & delete
        self.object = DepartmentFactory.create()

        # Create the client and login the user
        self.c = Client()
        self.c.login(
            username=self.superuser.username,
            password=self.superuser_pwd)

    def test_add_department(self):
        """Test that we can add a new object."""

        url = reverse('team-admin:department-add')

        # Test that the page load first
        response = self.c.get(url)
        self.assertEqual(response.status_code, 200)

        # Send data
        data = {
            "name": "Fun and games!",
        }
        response = self.c.post(url, data)
        self.assertEqual(response.status_code, 302)

        # Get the latest added object
        obj = Department.objects.filter().latest('id')
        self.assertEqual(obj.name, "Fun and games!")

    def test_update_department(self):
        """Test that we can update an existing object."""

        url = reverse(
            'team-admin:department-update',
            kwargs={
                'pk': self.object.id
            }
        )

        # Test that the page load first
        response = self.c.get(url)
        self.assertEqual(response.status_code, 200)

        # Send data
        data = {
            "order_id": "<<SETME>>",
            "name": "Fun and games",
        }
        response = self.c.post(url, data)
        self.assertEqual(response.status_code, 302)

        # Get the latest added object
        obj = Department.objects.get(id=self.object.id)

        self.assertEqual(obj.name, "Fun and games")

    def test_retrieve_department(self):
        """Test that we can retrieve an object from its ID."""

        url = reverse(
            'team-admin:department-detail',
            kwargs={
                'pk': self.object.id
            }
        )

        # Test that the page load first
        response = self.c.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_department(self):
        """Test that we can list objects."""

        url = reverse('team-admin:department-list')

        # Test that the page load first
        response = self.c.get(url)
        self.assertEqual(response.status_code, 200)

    def test_delete_department(self):
        """Test that we can delete an object."""

        url = reverse(
            'team-admin:department-delete',
            kwargs={
                'pk': self.object.id
            }
        )

        # Test that the page load first
        response = self.c.get(url)
        self.assertEqual(response.status_code, 200)

        # Action detail with POST call
        response = self.c.post(url)
        self.assertEqual(response.status_code, 302)

        # Test that the record has been deleted
        obj = Department.objects.filter(id=self.object.id)
        self.assertEqual(obj.count(), 0)
