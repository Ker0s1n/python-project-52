from django.contrib.auth import get_user_model
from django.test import Client, TestCase


class UserTestCase(TestCase):
    fixtures = ["test_users.yaml"]

    def setUp(self):
        self.client = Client()
        self.user1 = get_user_model().objects.get(id=1)
        self.user2 = get_user_model().objects.get(id=2)
        self.valid_user_data = {
            "first_name": "Rodion",
            "last_name": "Raskolnikov",
            "username": "Tvar",
            "email": "topor@dostoevskiy.ru",
            "password1": "Have_permission",
            "password2": "Have_permission",
        }
        self.update_user_data = {
            "first_name": "Eva",
            "last_name": "Polna",
            "username": "Golden_grammofon",
            "email": "evapolna@rukivverx.ru",
            "password1": "Guest_from_future",
            "password2": "Guest_from_future",
        }


class UserModelTest(UserTestCase):
    def test_create_user(self):
        response = self.client.get("/users/create/")
        self.assertEqual(response.status_code, 200)

        response = self.client.post(
            "/users/create/",
            self.valid_user_data,
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.count(), 3)
        self.assertEqual(
            get_user_model().objects.filter(pk=3)[0].username, "Tvar"
        )
