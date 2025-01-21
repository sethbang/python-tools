# Python Scripts Collection

A collection of utility scripts for file operations, directory management, and format conversions.

## Scripts Overview

### combine_markdown.py
Combines multiple markdown files into a single master file. Each file's content is separated with clear markers indicating the start and end of each source file.
- Usage: Run the script and provide the repository path and output filename when prompted.

### combine-text.py
Combines multiple text files from a selected directory into a single text file, with clear separation between contents.
- Usage: Run the script and select the directory containing the text files through the GUI dialog.

### delete_files_in_subdirs.py
Deletes all files within a selected directory and its subdirectories. Includes a confirmation dialog for safety.
- Usage: Run the script and select the target directory through the GUI dialog.

### demos.py
A GUI application that provides easy access to various file operations:
- Delete files in subdirectories
- Add prefix to all files in a directory
- Features a clean interface with clear buttons for each operation

### file_rename.py
Finds the largest file in a directory and renames it to match the directory name while preserving the file extension.
- Usage: Run the script and select the target directory through the GUI dialog.

### file_utilities.py
A collection of utility functions for file operations:
- `get_file_list`: Lists files in a directory with count
- `get_root_dir`: Opens directory selection dialog
- `get_file_path`: Opens single file selection dialog
- `get_file_paths`: Opens multiple file selection dialog

### image-search.py
Performs Google image searches and downloads results to a specified directory. Creates a results.txt file with detailed image information.
- Requires: SerpAPI key
- Usage: Run the script and select the save directory through the GUI dialog.

### merge_md.py
Merges multiple markdown files from a directory into a single file, adding separators and headers for clarity.
- Default input directory: './endpoints'
- Default output: './nba_live_endpoints.md'

### prefix_rename.py
Adds a specified prefix to all files within a selected directory.
- Features a GUI interface for prefix input
- Includes confirmation dialog before renaming

### process_subdirs.py
Processes subdirectories with a specified function (default: rename largest file).
- Usage: Run the script and select the root directory through the GUI dialog.

### tree_writer.py
Generates directory structure documentation in multiple formats:
- Supported formats: txt, html, pdf, json, yaml, natural language
- Features:
  - Customizable depth
  - Hidden file/directory filtering
  - Multiple output formats
- Usage: `python tree_writer.py [-p PATH] [-o OUTPUT] [-f FORMAT] [-d DEPTH]`

### txt-to-pdf.py
Converts text files to PDF format.
- Features:
  - Custom input/output path selection
  - Uses Arial font, size 12
  - Left-aligned text formatting

## Dependencies
- tkinter (GUI components)
- fpdf (PDF generation)
- reportlab (PDF generation)
- jinja2 (HTML template rendering)
- yaml (YAML file handling)
- serpapi (Google image search API)

## Installation
1. Clone the repository
2. Install required dependencies:
```bash
pip install fpdf reportlab jinja2 pyyaml google-search-results
```

## Testing
The repository includes a comprehensive test suite for the Python scripts. Tests are located in the `tests` directory.

### Dependencies for Testing
Before running tests, ensure you have all required dependencies installed:
```bash
pip install reportlab pyyaml
brew install tcl-tk  # For macOS users
```

### Running Tests
To run all tests:
```bash
python tests/run_tests.py
```

This will execute all test cases and provide a summary of:
- Total tests run
- Number of failures
- Number of errors
- Number of skipped tests

The test suite uses Python's unittest framework and includes mocking for GUI components to enable headless testing.

### Available Test Suites
- `test_file_utilities.py`: Tests for basic file operation utilities
- `test_file_rename.py`: Tests for file renaming functionality
- `test_combine_markdown.py`: Tests for markdown file combination
- `test_tree_writer.py`: Tests for directory structure generation and output formats

### Writing New Tests
When adding new scripts or modifying existing ones, please ensure to:
1. Create corresponding test files in the `tests` directory
2. Follow the naming convention `test_*.py`
3. Use Python's unittest framework
4. Include both positive and negative test cases
5. Clean up any temporary files/directories created during tests

## Future Development
See [ROADMAP.md](ROADMAP.md) for a detailed list of recommended scripts and tools we plan to build. This includes:
- Code generation and templating tools
- Development workflow automation
- Testing and quality assurance utilities
- Documentation generators
- Deployment and DevOps tools
- Data processing utilities
- Security tools
- Monitoring and maintenance systems

Each proposed tool includes detailed features, implementation guidelines, and integration priorities.

## License
See LICENSE file for details.