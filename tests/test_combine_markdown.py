import unittest
import os
import tempfile
import shutil
import json
from src.combine_markdown import collect_markdown_files, combine_markdown_files, read_reading_order, is_valid_file

class TestCombineMarkdown(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = tempfile.mkdtemp()
        
        # Create test files
        self.test_files = {
            'test1.md': '# Test 1\nContent 1',
            'test2.md': '# Test 2\nContent 2',
            'test3.txt': 'Text file content',
            'test4.pdf': 'PDF content',
            'master.md': 'Previous master content',
            'subdir/test5.md': '# Test 5\nContent 5',
            'subdir/test6.txt': 'More text content'
        }
        
        # Create files and their content
        for file_path, content in self.test_files.items():
            full_path = os.path.join(self.test_dir, file_path)
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            with open(full_path, 'w') as f:
                f.write(content)

    def tearDown(self):
        # Clean up the temporary directory
        shutil.rmtree(self.test_dir)

    def test_is_valid_file(self):
        # Test valid files with full paths
        output_file = os.path.join(self.test_dir, 'output.md')
        self.assertTrue(is_valid_file(
            os.path.join(self.test_dir, 'test1.md'), 
            output_file
        ))
        self.assertTrue(is_valid_file(
            os.path.join(self.test_dir, 'test3.txt'), 
            output_file
        ))
        
        # Test invalid files with full paths
        self.assertFalse(is_valid_file(
            os.path.join(self.test_dir, 'test4.pdf'), 
            output_file
        ))
        self.assertFalse(is_valid_file(
            os.path.join(self.test_dir, 'master.md'), 
            output_file
        ))
        self.assertFalse(is_valid_file(
            output_file, 
            output_file
        ))

    def test_collect_markdown_and_text_files(self):
        # Test collecting markdown and text files
        output_file = os.path.join(self.test_dir, 'new_master.md')
        files = collect_markdown_files(self.test_dir, output_file=output_file)
        
        # Sort files to ensure consistent order for comparison
        files = sorted(files)
        
        # Expected valid files (2 md + 2 txt, excluding master.md)
        expected_files = sorted([
            os.path.join(self.test_dir, 'test1.md'),
            os.path.join(self.test_dir, 'test2.md'),
            os.path.join(self.test_dir, 'test3.txt'),
            os.path.join(self.test_dir, 'subdir/test6.txt')
        ])
        
        # Verify we got exactly the expected files
        self.assertEqual([os.path.normpath(f) for f in files],
                        [os.path.normpath(f) for f in expected_files])
        
        # Verify master.md and pdf files were not collected
        master_file = os.path.join(self.test_dir, 'master.md')
        pdf_file = os.path.join(self.test_dir, 'test4.pdf')
        self.assertNotIn(master_file, files)
        self.assertNotIn(pdf_file, files)

    def test_combine_markdown_and_text_files(self):
        # Create output file path
        output_file = os.path.join(self.test_dir, 'combined.md')
        
        # Get valid files
        files = collect_markdown_files(self.test_dir, output_file=output_file)
        
        # Combine the files
        combine_markdown_files(files, output_file)
        
        # Verify output file exists
        self.assertTrue(os.path.exists(output_file))
        
        # Read combined content
        with open(output_file, 'r') as f:
            content = f.read()
        
        # Verify all valid content is present
        self.assertIn('# Test 1', content)
        self.assertIn('Content 1', content)
        self.assertIn('# Test 2', content)
        self.assertIn('Content 2', content)
        self.assertIn('Text file content', content)
        self.assertIn('More text content', content)
        
        # Verify invalid content is not present
        self.assertNotIn('PDF content', content)
        self.assertNotIn('Previous master content', content)
        
        # Verify file markers are present
        self.assertIn('START OF FILE:', content)
        self.assertIn('END OF FILE:', content)

    def test_reading_order_json_present(self):
        # Create a reading_order.json file
        reading_order_content = {
            "reading_order": [
                {"document": "test2.md"},
                {"document": "test3.txt"},
                {"document": "subdir/test5.md"}
            ]
        }
        reading_order_path = os.path.join(self.test_dir, 'reading_order.json')
        with open(reading_order_path, 'w') as f:
            json.dump(reading_order_content, f)

        # Read the reading order
        reading_order = read_reading_order(self.test_dir)
        
        # Collect files with reading order
        output_file = os.path.join(self.test_dir, 'new_master.md')
        files = collect_markdown_files(self.test_dir, reading_order, output_file)

        # Expected order for the first three files
        expected_order = [
            os.path.join(self.test_dir, 'test2.md'),
            os.path.join(self.test_dir, 'test3.txt'),
            os.path.join(self.test_dir, 'subdir/test5.md')
        ]
        
        # Check that the first three files match the expected order
        self.assertEqual(
            [os.path.normpath(p) for p in files[:3]], 
            [os.path.normpath(p) for p in expected_order]
        )
        
        # Verify total number of files (3 ordered + 1 remaining valid file)
        self.assertEqual(len(files), 4)
        
        # Verify the remaining file is test1.md or test6.txt
        remaining_file = files[3]
        self.assertTrue(
            remaining_file.endswith('test1.md') or 
            remaining_file.endswith('test6.txt')
        )

    def test_reading_order_json_invalid(self):
        # Create an invalid reading_order.json file
        reading_order_path = os.path.join(self.test_dir, 'reading_order.json')
        with open(reading_order_path, 'w') as f:
            f.write('invalid json content')

        # Read the reading order (should return None for invalid JSON)
        reading_order = read_reading_order(self.test_dir)
        self.assertIsNone(reading_order)

        # Collect files without reading order (should fall back to default behavior)
        output_file = os.path.join(self.test_dir, 'new_master.md')
        files = collect_markdown_files(self.test_dir, reading_order, output_file)
        
        # Should find 4 valid files, sorted alphabetically
        expected_files = sorted([
            os.path.join(self.test_dir, 'test1.md'),
            os.path.join(self.test_dir, 'test2.md'),
            os.path.join(self.test_dir, 'test3.txt'),
            os.path.join(self.test_dir, 'subdir/test6.txt')
        ])
        self.assertEqual(
            [os.path.normpath(f) for f in files],
            [os.path.normpath(f) for f in expected_files]
        )

    def test_reading_order_missing_files(self):
        # Create a reading_order.json with non-existent files
        reading_order_content = {
            "reading_order": [
                {"document": "nonexistent.md"},
                {"document": "test1.md"},
                {"document": "another_missing.md"}
            ]
        }
        reading_order_path = os.path.join(self.test_dir, 'reading_order.json')
        with open(reading_order_path, 'w') as f:
            json.dump(reading_order_content, f)

        # Read the reading order
        reading_order = read_reading_order(self.test_dir)
        
        # Collect files with reading order
        output_file = os.path.join(self.test_dir, 'new_master.md')
        files = collect_markdown_files(self.test_dir, reading_order, output_file)

        # Verify test1.md is first (it's the only existing file in reading_order)
        self.assertTrue(files[0].endswith('test1.md'))
        
        # Verify we got all valid files
        self.assertEqual(len(files), 4)
        
        # Verify all files are valid
        for file in files:
            self.assertTrue(
                file.endswith('.md') or file.endswith('.txt')
            )
            self.assertNotIn('master.md', file)

if __name__ == '__main__':
    unittest.main()