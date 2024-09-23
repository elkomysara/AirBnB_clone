#!/usr/bin/python3
"""Unittests for the console (command interpreter)"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User


class TestConsole(unittest.TestCase):
    """Test class for console.py"""

    def setUp(self):
        """Set up for each test"""
        # Optionally clear storage to avoid data conflicts
        storage.all().clear()

    def tearDown(self):
        """Tear down after each test"""
        storage.all().clear()

    def test_create_with_valid_class(self):
        """Test create command with valid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            self.assertIn("User", storage.all())
            self.assertTrue(len(f.getvalue().strip()) > 0)

    def test_create_with_missing_class(self):
        """Test create command with missing class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_create_with_invalid_class(self):
        """Test create command with invalid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create MyModel")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_show_with_valid_id(self):
        """Test show command with valid class and id"""
        obj = User()
        obj.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show User {obj.id}")
            self.assertIn(obj.id, f.getvalue().strip())

    def test_show_with_missing_class(self):
        """Test show command with missing class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_show_with_invalid_class(self):
        """Test show command with invalid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show MyModel")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_show_with_missing_id(self):
        """Test show command with missing id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_show_with_invalid_id(self):
        """Test show command with invalid id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User invalid_id")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_destroy_with_valid_id(self):
        """Test destroy command with valid class and id"""
        obj = User()
        obj.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy User {obj.id}")
            self.assertNotIn(obj.id, storage.all())

    def test_destroy_with_missing_class(self):
        """Test destroy command with missing class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_destroy_with_invalid_class(self):
        """Test destroy command with invalid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy MyModel")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_destroy_with_invalid_id(self):
        """Test destroy command with invalid id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User invalid_id")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_all_with_valid_class(self):
        """Test all command with a valid class"""
        obj = User()
        obj.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all User")
            self.assertIn(f"[User] ({obj.id})", f.getvalue().strip())

    def test_all_with_invalid_class(self):
        """Test all command with an invalid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all MyModel")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_all_with_no_class(self):
        """Test all command with no class"""
        obj = User()
        obj.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            self.assertIn(f"[User] ({obj.id})", f.getvalue().strip())

    def test_update_with_valid_args(self):
        """Test update command with valid args"""
        obj = User()
        obj.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update User {obj.id} first_name Betty")
            self.assertEqual(storage.all()[f"User.{obj.id}"].first_name, "Betty")

    def test_update_with_invalid_class(self):
        """Test update command with invalid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update MyModel 1234-1234 first_name Betty")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_update_with_invalid_id(self):
        """Test update command with invalid id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User invalid_id first_name Betty")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_update_with_missing_args(self):
        """Test update command with missing arguments"""
        obj = User()
        obj.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update User {obj.id}")
            self.assertEqual(f.getvalue().strip(), "** attribute name missing **")

    def test_update_with_dictionary(self):
        """Test update command with a dictionary"""
        obj = User()
        obj.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update User {obj.id} {{'first_name': 'John', 'age': 30}}")
            self.assertEqual(storage.all()[f"User.{obj.id}"].first_name, "John")
            self.assertEqual(storage.all()[f"User.{obj.id}"].age, 30)


if __name__ == "__main__":
    unittest.main()
