import unittest
import os
import tempfile
import shutil
import json
import yaml
from src.tree_writer import (
    generate_directory_structure,
    describe_directory_in_natural_language,
    is_hidden,
    save_to_file
)

class TestTreeWriter(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory structure for testing
        self.test_dir = tempfile.mkdtemp()
        
        # Create a test directory structure
        os.makedirs(os.path.join(self.test_dir, 'dir1'))
        os.makedirs(os.path.join(self.test_dir, 'dir2', 'subdir'))
        
        # Create some test files
        self.create_test_file(os.path.join(self.test_dir, 'file1.txt'))
        self.create_test_file(os.path.join(self.test_dir, 'dir1', 'file2.txt'))
        self.create_test_file(os.path.join(self.test_dir, 'dir2', 'file3.txt'))
        self.create_test_file(os.path.join(self.test_dir, 'dir2', 'subdir', 'file4.txt'))
        self.create_test_file(os.path.join(self.test_dir, '.hidden_file'))
        os.makedirs(os.path.join(self.test_dir, '.hidden_dir'))

    def tearDown(self):
        # Clean up the temporary directory
        shutil.rmtree(self.test_dir)

    def create_test_file(self, path):
        with open(path, 'w') as f:
            f.write('test content')

    def test_generate_directory_structure(self):
        # Test with unlimited depth
        structure = generate_directory_structure(self.test_dir, -1)
        
        # Verify structure format
        self.assertIsInstance(structure, list)
        self.assertTrue(len(structure) > 0)
        
        # Verify structure contents
        root_dir = structure[0]
        self.assertIn('dir', root_dir)
        self.assertIn('level', root_dir)
        self.assertIn('files', root_dir)
        self.assertIn('subdirs', root_dir)
        
        # Verify hidden files/dirs are excluded
        self.assertNotIn('.hidden_file', root_dir['files'])
        self.assertNotIn('.hidden_dir', root_dir['subdirs'])

    def test_generate_directory_structure_with_depth_limit(self):
        # Test with depth limit of 1
        structure = generate_directory_structure(self.test_dir, 1)
        
        # Should only include root and immediate subdirectories
        max_level = max(item['level'] for item in structure)
        self.assertEqual(max_level, 1)

    def test_describe_directory_in_natural_language(self):
        structure = generate_directory_structure(self.test_dir, -1)
        description = describe_directory_in_natural_language(structure)
        
        # Verify description is a string
        self.assertIsInstance(description, str)
        
        # Verify description contains key information
        self.assertIn('contains', description)
        self.assertIn('files', description)
        self.assertIn('subdirectories', description)

    def test_is_hidden(self):
        # Test hidden file/directory detection
        self.assertTrue(is_hidden('.hidden_file'))
        self.assertTrue(is_hidden('.hidden_dir'))
        self.assertFalse(is_hidden('visible_file'))
        self.assertFalse(is_hidden('visible_dir'))

    def test_save_to_file_json(self):
        structure = generate_directory_structure(self.test_dir, -1)
        output_file = os.path.join(self.test_dir, 'output')
        
        # Test JSON output
        save_to_file(structure, output_file, 'json')
        json_file = output_file + '.json'
        
        # Verify JSON file exists and is valid
        self.assertTrue(os.path.exists(json_file))
        with open(json_file, 'r') as f:
            data = json.load(f)
        self.assertIsInstance(data, list)

    def test_save_to_file_yaml(self):
        structure = generate_directory_structure(self.test_dir, -1)
        output_file = os.path.join(self.test_dir, 'output')
        
        # Test YAML output
        save_to_file(structure, output_file, 'yaml')
        yaml_file = output_file + '.yaml'
        
        # Verify YAML file exists and is valid
        self.assertTrue(os.path.exists(yaml_file))
        with open(yaml_file, 'r') as f:
            data = yaml.safe_load(f)
        self.assertIsInstance(data, list)

    def test_save_to_file_txt(self):
        structure = generate_directory_structure(self.test_dir, -1)
        output_file = os.path.join(self.test_dir, 'output')
        
        # Test TXT output
        save_to_file(structure, output_file, 'txt')
        txt_file = output_file + '_t.txt'
        
        # Verify TXT file exists and has content
        self.assertTrue(os.path.exists(txt_file))
        with open(txt_file, 'r') as f:
            content = f.read()
        self.assertGreater(len(content), 0)

if __name__ == '__main__':
    unittest.main()