import unittest
import os
import tempfile
import shutil
from unittest.mock import patch, MagicMock
import sys
sys.modules['tkinter'] = MagicMock()
from src.file_rename import find_and_rename_largest_file

class TestFileRename(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = tempfile.mkdtemp()
        
        # Create test files of different sizes
        self.small_file = os.path.join(self.test_dir, 'small.txt')
        self.large_file = os.path.join(self.test_dir, 'large.txt')
        
        # Write content to create files of different sizes
        with open(self.small_file, 'w') as f:
            f.write('small content')
        
        with open(self.large_file, 'w') as f:
            f.write('large content' * 1000)  # Make this file larger
        
        # Store the directory name for later comparison
        self.dir_name = os.path.basename(self.test_dir)

    def tearDown(self):
        # Clean up the temporary directory
        shutil.rmtree(self.test_dir)

    def test_find_and_rename_largest_file(self):
        # Call the function to test
        find_and_rename_largest_file(self.test_dir)
        
        # Get list of files in directory
        files = os.listdir(self.test_dir)
        
        # Check that the largest file was renamed to directory name
        expected_name = f"{self.dir_name}.txt"
        self.assertIn(expected_name, files)
        
        # Verify the small file still exists
        self.assertIn('small.txt', files)
        
        # Verify the large file was renamed
        self.assertNotIn('large.txt', files)
        
        # Verify the total number of files hasn't changed
        self.assertEqual(len(files), 2)
        
        # Verify the renamed file is the largest
        renamed_file_path = os.path.join(self.test_dir, expected_name)
        small_file_path = os.path.join(self.test_dir, 'small.txt')
        self.assertGreater(
            os.path.getsize(renamed_file_path),
            os.path.getsize(small_file_path)
        )

    def test_empty_directory(self):
        # Create an empty directory
        empty_dir = tempfile.mkdtemp()
        try:
            # Should not raise any exceptions
            find_and_rename_largest_file(empty_dir)
            # Verify directory is still empty
            self.assertEqual(len(os.listdir(empty_dir)), 0)
        finally:
            shutil.rmtree(empty_dir)

    @patch('file_rename.filedialog')
    def test_main_function(self, mock_filedialog):
        from src.file_rename import main
        
        # Create a temporary directory with a test file
        test_dir = tempfile.mkdtemp()
        test_file = os.path.join(test_dir, 'test.txt')
        with open(test_file, 'w') as f:
            f.write('test content')
        
        try:
            # Mock the file dialog to return our temporary directory
            mock_filedialog.askdirectory.return_value = test_dir
            
            # Mock Tk to prevent GUI creation
            with patch('file_rename.tk.Tk'):
                main()
                mock_filedialog.askdirectory.assert_called_once()
                
                # Verify the file was renamed
                files = os.listdir(test_dir)
                self.assertEqual(len(files), 1)
                self.assertEqual(files[0], os.path.basename(test_dir) + '.txt')
        finally:
            shutil.rmtree(test_dir)

if __name__ == '__main__':
    unittest.main()