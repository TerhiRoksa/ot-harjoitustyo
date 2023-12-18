import unittest
from services.user_service import UserService
from repositories.database import SimpleLoginSystemDB


class TestFoodService(unittest.TestCase):

    def setUp(self):
        self.login_system = SimpleLoginSystemDB()
        self.user_service = UserService(self.login_system)

    def test_register_user(self):
        username = "tonttu"
        password = "ukko"
        self.user_service.register_user(username, password)
        result = self.user_service.get_user(username)
        self.assertEqual(result, self.user_service.get_user("tonttu"))
