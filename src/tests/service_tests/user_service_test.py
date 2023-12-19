import unittest
from services.user_service import UserService
from repositories.database import StorageSystemDB


class TestFoodService(unittest.TestCase):

    def setUp(self):
        self.storage_system = StorageSystemDB()
        self.user_service = UserService(self.storage_system)

    def test_register_user(self):
        username = "tonttu"
        password = "ukko"
        self.user_service.register_user(username, password)
        result = self.user_service.get_user(username)
        self.assertEqual(result, self.user_service.get_user("tonttu"))
