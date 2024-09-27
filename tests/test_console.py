#!/usr/bin/python3
"""Unittest for the HBNBCommand class"""
import unittest
from console import HBNBCommand
from models import storage
from io import StringIO
from unittest.mock import patch

class TestHBNBCommandCreate(unittest.TestCase):
    """Test the create method with parameters"""

    def test_create_with_parameters(self):
        """Test object creation with multiple parameters"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create State name="California"')
            state_id = f.getvalue().strip()
            all_states = storage.all()
            self.assertIn(f'State.{state_id}', all_states)
            self.assertEqual(all_states[f'State.{state_id}'].name, "California")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Place city_id="0001" user_id="0001" name="My_little_house" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297')
            place_id = f.getvalue().strip()
            all_places = storage.all()
            self.assertIn(f'Place.{place_id}', all_places)
            place = all_places[f'Place.{place_id}']
            self.assertEqual(place.name, "My little house")
            self.assertEqual(place.number_rooms, 4)
            self.assertEqual(place.latitude, 37.773972)

if __name__ == '__main__':
    unittest.main()
