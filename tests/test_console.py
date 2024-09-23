#!/usr/bin/python3
"""Unittests for the console."""

import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage
from models.user import User

class TestConsole(unittest.TestCase):
    """Test the HBNB console."""

    def test_create_with_valid_class(self):
        """Test create command with valid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            created_id = f.getvalue().strip()
            key = f"User.{created_id}"
            self.assertIn(key, storage.all())
            self.assertTrue(len(created_id) > 0)

    def test_update_with_dictionary(self):
        """Test update command with a dictionary"""
        obj = User()
        obj.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.update('{obj.id}', {{'first_name': 'John', 'age': 89}})")
            updated_obj = storage.all()[f"User.{obj.id}"]
            self.assertEqual(updated_obj.first_name, "John")
            self.assertEqual(updated_obj.age, 89)

    def test_update_with_missing_args(self):
        """Test update command with missing arguments"""
        obj = User()
        obj.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update User {obj.id}")
            self.assertEqual(f.getvalue().strip(), "** attribute name missing **")

if __name__ == "__main__":
    unittest.main()
