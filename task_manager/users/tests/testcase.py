from django.contrib.auth import get_user_model
from django.test import Client, TestCase


class UserTestCase(TestCase):
    fixtures = ["test_users.yaml"]

    def setUp(self):
        self.client = Client()
        self.user1 = get_user_model().objects.get(id=1)
        self.user2 = get_user_model().objects.get(id=2)
        self.user_count = get_user_model().objects.count()
        self.valid_user_data = {
            "first_name": "Rodion",
            "last_name": "Raskolnikov",
            "username": "Tvar",
            "password1": "Have_permission",
            "password2": "Have_permission",
        }
        self.update_user_data = {
            "first_name": "Eva",
            "last_name": "Polna",
            "username": "Golden_grammofon",
            "password1": "Guest_from_future",
            "password2": "Guest_from_future",
        }
