#!/usr/bin/python3
"""Unit tests for BaseModel"""
import unittest
from models.base_model import BaseModel
import datetime
import json
import os


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel"""

    def setUp(self):
        """Set up test environment"""
        self.model = BaseModel()

    def tearDown(self):
        """Clean up test environment"""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_default_constructor(self):
        """Test default constructor"""
        self.assertIsInstance(self.model, BaseModel)

    def test_kwargs_constructor(self):
        """Test constructor with **kwargs"""
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertIsNot(new_model, self.model)
        self.assertEqual(new_model.to_dict(), model_dict)

    def test_kwargs_constructor_invalid(self):
        """Test constructor with invalid **kwargs"""
        kwargs = {'invalid_key': 'value'}
        with self.assertRaises(TypeError):
            BaseModel(**kwargs)

    def test_id_type(self):
        """Test id type"""
        self.assertIsInstance(self.model.id, str)

    def test_created_at_type(self):
        """Test created_at type"""
        self.assertIsInstance(self.model.created_at, datetime.datetime)

    def test_updated_at_type(self):
        """Test updated_at type"""
        self.assertIsInstance(self.model.updated_at, datetime.datetime)

    def test_save(self):
        """Test save method"""
        self.model.save()
        self.assertTrue(os.path.isfile('file.json'))
        with open('file.json', 'r') as file:
            data = json.load(file)
            key = '{}.{}'.format(type(self.model).__name__, self.model.id)
            self.assertEqual(data[key], self.model.to_dict())

    def test_str_representation(self):
        """Test __str__ method"""
        expected_str = '[{}] ({}) {}'.format(
            type(self.model).__name__, self.model.id, self.model.__dict__
        )
        self.assertEqual(str(self.model), expected_str)

    def test_to_dict(self):
        """Test to_dict method"""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], type(self.model).__name__)
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_from_dict(self):
        """Test from_dict method"""
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertIsNot(new_model, self.model)
        self.assertEqual(new_model.to_dict(), model_dict)
        self.assertIsInstance(new_model.id, str)
        self.assertIsInstance(new_model.created_at, datetime.datetime)
        self.assertIsInstance(new_model.updated_at, datetime.datetime)
        self.assertEqual(new_model.id, self.model.id)
        self.assertEqual(new_model.created_at, self.model.created_at)
        self.assertEqual(new_model.updated_at, self.model.updated_at)


if __name__ == '__main__':
    unittest.main()

