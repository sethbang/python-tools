import unittest
import os
import tempfile
import shutil
from unittest.mock import patch, MagicMock
import sys
sys.modules['tkinter'] = MagicMock()
from src.file_utilities import get_file_list

class TestFileUtilities(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = tempfile.mkdtemp()
        
        # Create some test files
        self.test_files = ['test1.txt', 'test2.txt', 'test3.md']
        for file_name in self.test_files:
            with open(os.path.join(self.test_dir, file_name), 'w') as f:
                f.write('test content')

    def tearDown(self):
        # Clean up the temporary directory
        shutil.rmtree(self.test_dir)

    def test_get_file_list(self):
        # Test get_file_list function
        result = get_file_list(self.test_dir)
        
        # Check if the result is a dictionary
        self.assertIsInstance(result, dict)
        
        # Check if it has the required keys
        self.assertIn('files', result)
        self.assertIn('count', result)
        
        # Check if the count matches the number of test files
        self.assertEqual(result['count'], len(self.test_files))
        
        # Check if all test files are in the result
        for file_name in self.test_files:
            self.assertIn(file_name, result['files'])

    def test_get_file_list_empty_directory(self):
        # Create an empty directory
        empty_dir = tempfile.mkdtemp()
        
        try:
            # Test get_file_list with empty directory
            result = get_file_list(empty_dir)
            
            # Check if the result is correct for empty directory
            self.assertEqual(result['count'], 0)
            self.assertEqual(len(result['files']), 0)
        finally:
            # Clean up
            shutil.rmtree(empty_dir)

    @patch('file_utilities.filedialog')
    def test_get_root_dir(self, mock_filedialog):
        from src.file_utilities import get_root_dir
        expected_path = '/test/path'
        mock_filedialog.askdirectory.return_value = expected_path
        
        result = get_root_dir()
        self.assertEqual(result, expected_path)
        mock_filedialog.askdirectory.assert_called_once()

    @patch('file_utilities.filedialog')
    def test_get_file_path(self, mock_filedialog):
        from src.file_utilities import get_file_path
        expected_path = '/test/file.txt'
        mock_filedialog.askopenfilename.return_value = expected_path
        
        result = get_file_path()
        self.assertEqual(result, expected_path)
        mock_filedialog.askopenfilename.assert_called_once()

    @patch('file_utilities.filedialog')
    def test_get_file_paths(self, mock_filedialog):
        from src.file_utilities import get_file_paths
        expected_paths = ('/test/file1.txt', '/test/file2.txt')
        mock_filedialog.askopenfilenames.return_value = expected_paths
        
        result = get_file_paths()
        self.assertEqual(result, expected_paths)
        mock_filedialog.askopenfilenames.assert_called_once()

if __name__ == '__main__':
    unittest.main()