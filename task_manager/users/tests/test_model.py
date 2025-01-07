from django.contrib.auth import get_user_model

from task_manager.users.tests.testcase import UserTestCase


class UserModelTest(UserTestCase):
    def test_user_creation(self):
        get_user_model().objects.create(
            first_name=self.valid_user_data["first_name"],
            last_name=self.valid_user_data["last_name"],
            username=self.valid_user_data["username"],
            password=self.valid_user_data["password1"],
        )
        user = get_user_model().objects.get(
            username=self.valid_user_data["username"]
        )
        self.assertEqual(user.username, self.valid_user_data["username"])
        self.assertEqual(user.first_name, self.valid_user_data["first_name"])
        self.assertEqual(user.last_name, self.valid_user_data["last_name"])
        self.assertEqual(
            str(user),
            self.valid_user_data["first_name"]
            + " "
            + self.valid_user_data["last_name"],
        )

    def test_duplicate_username(self):
        get_user_model().objects.create(
            first_name=self.valid_user_data["first_name"],
            last_name=self.valid_user_data["last_name"],
            username=self.valid_user_data["username"],
            password=self.valid_user_data["password1"],
        )
        with self.assertRaises(Exception):
            get_user_model().objects.create(
                first_name="Sonya",
                last_name="Marmeladova",
                username="Tvar",
                password="Havent_permission",
            )
