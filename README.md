# Python Scripts Collection 🐍

[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)](tests/)

A powerful collection of Python utility scripts for file operations, directory management, and format conversions. Streamline your workflow with easy-to-use tools for common development tasks.

## 📑 Table of Contents
- [Quick Start](#-quick-start)
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Testing](#-testing)
- [Contributing](#-contributing)
- [Future Development](#-future-development)
- [Troubleshooting](#-troubleshooting)
- [License](#-license)

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/python-scripts.git

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run a script (example: tree_writer)
python src/tree_writer.py -p /path/to/directory -o output.txt -f txt
```

## ✨ Features

### File Operations
- **combine_markdown.py**: Merge multiple markdown files into a single document
- **combine-text.py**: Concatenate text files with clear separators
- **delete_files_in_subdirs.py**: Safely remove files in directories
- **file_rename.py**: Smart file renaming based on directory names

### Directory Management
- **tree_writer.py**: Generate directory structure documentation
  ```bash
  python tree_writer.py -p ./my_project -o structure.txt -f txt -d 3
  ```
- **process_subdirs.py**: Batch process subdirectories
- **prefix_rename.py**: Add prefixes to files in bulk

### Format Conversions
- **txt-to-pdf.py**: Convert text files to professional PDFs
- **merge_md.py**: Combine and format markdown documentation

### Utility Tools
- **demos.py**: GUI interface for common operations
- **file_utilities.py**: Core utility functions
- **image-search.py**: Automated image search and download

## 🔧 Installation

1. Ensure Python 3.6+ is installed
2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install fpdf reportlab jinja2 pyyaml google-search-results
   ```

4. Additional system requirements:
   - macOS: `brew install tcl-tk`
   - Linux: `sudo apt-get install python3-tk`
   - Windows: Tkinter included with Python

## 🎯 Usage

### Tree Writer Example
```python
from src.tree_writer import generate_tree

# Generate directory structure in JSON format
generate_tree(
    path="./my_project",
    output="structure.json",
    format="json",
    depth=3
)
```

### Markdown Combiner Example
```python
from src.combine_markdown import combine_files

# Merge markdown files
combine_files(
    input_dir="./docs",
    output_file="combined.md"
)
```

## 🧪 Testing

Run the comprehensive test suite:

```bash
python tests/run_tests.py
```

### Test Coverage
- ✅ File operations
- ✅ Directory management
- ✅ Format conversions
- ✅ Utility functions

### Writing Tests
1. Create test files in `tests/` directory
2. Follow naming convention: `test_*.py`
3. Use unittest framework
4. Include positive and negative cases
5. Clean up test artifacts

## 👥 Contributing

1. Fork the repository
2. Create a feature branch
3. Write clean, documented code
4. Add tests for new functionality
5. Submit a pull request

### Code Style
- Follow PEP 8 guidelines
- Add docstrings to functions
- Keep functions focused and modular
- Include type hints

## 🔮 Future Development

See [ROADMAP.md](docs/ROADMAP.md) for detailed plans including:
- Code generation tools
- Workflow automation
- Testing utilities
- Documentation generators
- DevOps tools
- Data processing
- Security features
- Monitoring systems

## 🔍 Troubleshooting

### Common Issues
1. **GUI Not Working**
   - Ensure Tkinter is installed
   - Check Python version compatibility

2. **PDF Generation Fails**
   - Verify fpdf/reportlab installation
   - Check write permissions

3. **Image Search Issues**
   - Verify SerpAPI key configuration
   - Check network connectivity

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](docs/LICENSE) file for details.