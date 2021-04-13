from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    """ The Method setUp, that is a pre requisite to testing things that requires Admin """

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@gmail.com", password="password1234"
        )

        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="test@gmail.com", password="123asdfg", name="Test Name "
        )

    def test_users_listed(self):
        """ Test that users are listed on users page """
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)