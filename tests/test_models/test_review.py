#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.text), str)

    def test_updated_at(self):
        """Test that updated_at is different after saving the object"""
        new = self.value()
        created_at = new.created_at
        # Call save to update the updated_at timestamp
        new.save()
        self.assertFalse(created_at == new.updated_at)
        self.assertTrue(created_at == new.created_at)
