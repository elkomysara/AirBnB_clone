#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def setUp(self):
        """Set up a BaseModel instance for testing"""
        self.model = BaseModel()

    def test_instance(self):
        """Test if the instance is of type BaseModel"""
        self.assertIsInstance(self.model, BaseModel)

    def test_attributes(self):
        """Test attributes of the BaseModel"""
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_save_method(self):
        """Test save method updates the updated_at attribute"""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict(self):
        """Test to_dict method creates correct dictionary representation"""
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], self.model.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()
