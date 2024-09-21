#!/usr/bin/python3
import unittest
from models.user import User

class TestUser(unittest.TestCase):
    """Test cases for the User class"""

    def setUp(self):
        """Set up a User instance for testing"""
        self.user = User()

    def test_instance(self):
        """Test if the instance is of type User"""
        self.assertIsInstance(self.user, User)

    def test_attributes(self):
        """Test attributes of the User"""
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")

if __name__ == '__main__':
    unittest.main()
