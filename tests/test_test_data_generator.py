#!/usr/bin/env python3
"""
Unit tests for the TestDataGenerator class.
"""

import unittest
import os
import csv
from datetime import datetime
from src.test_data_generator import TestDataGenerator, ColumnConfig

class TestTestDataGenerator(unittest.TestCase):
    """Test cases for TestDataGenerator functionality."""

    def setUp(self):
        """Set up test fixtures."""
        self.test_file = "test_output.csv"
        self.columns = [
            ColumnConfig(name="id", data_type="integer", min_value=1, max_value=10),
            ColumnConfig(name="name", data_type="string", pattern="test"),
            ColumnConfig(name="email", data_type="email"),
            ColumnConfig(name="score", data_type="float", min_value=0.0, max_value=100.0)
        ]
        self.generator = TestDataGenerator(self.columns)

    def tearDown(self):
        """Clean up test fixtures."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_initialization(self):
        """Test generator initialization."""
        self.assertEqual(len(self.generator.columns), 4)
        self.assertEqual(len(self.generator.data), 4)
        self.assertIn("id", self.generator.data)
        self.assertIn("name", self.generator.data)
        self.assertIn("email", self.generator.data)
        self.assertIn("score", self.generator.data)

    def test_generate_integer(self):
        """Test integer generation."""
        config = ColumnConfig(name="test", data_type="integer", min_value=1, max_value=10)
        value = self.generator._generate_integer(config)
        self.assertIsInstance(value, int)
        self.assertGreaterEqual(value, 1)
        self.assertLessEqual(value, 10)

    def test_generate_string(self):
        """Test string generation."""
        config = ColumnConfig(name="test", data_type="string", pattern="test_pattern")
        value = self.generator._generate_string(config)
        self.assertEqual(value, "test_pattern")

        # Test random string generation
        config = ColumnConfig(name="test", data_type="string")
        value = self.generator._generate_string(config)
        self.assertIsInstance(value, str)
        self.assertGreater(len(value), 0)

    def test_generate_email(self):
        """Test email generation."""
        config = ColumnConfig(name="test", data_type="email")
        value = self.generator._generate_email(config)
        self.assertIsInstance(value, str)
        self.assertIn("@", value)
        self.assertIn(".", value)

    def test_generate_float(self):
        """Test float generation."""
        config = ColumnConfig(name="test", data_type="float", min_value=0.0, max_value=1.0)
        value = self.generator._generate_float(config)
        self.assertIsInstance(value, float)
        self.assertGreaterEqual(value, 0.0)
        self.assertLessEqual(value, 1.0)

    def test_generate_data(self):
        """Test data generation."""
        num_rows = 5
        self.generator.generate_data(num_rows)
        
        for column in self.columns:
            self.assertEqual(len(self.generator.data[column.name]), num_rows)

    def test_save_to_csv(self):
        """Test CSV file generation."""
        num_rows = 5
        self.generator.generate_data(num_rows)
        self.generator.save_to_csv(self.test_file)

        self.assertTrue(os.path.exists(self.test_file))
        
        with open(self.test_file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)
            self.assertEqual(len(header), len(self.columns))
            
            rows = list(reader)
            self.assertEqual(len(rows), num_rows)

    def test_null_values(self):
        """Test null value generation."""
        columns = [
            ColumnConfig(name="nullable", data_type="string", null_probability=1.0)
        ]
        generator = TestDataGenerator(columns)
        generator.generate_data(10)
        
        self.assertTrue(all(v is None for v in generator.data["nullable"]))

if __name__ == '__main__':
    unittest.main()