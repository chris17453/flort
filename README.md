# Flort: File Concatenation and Project Overview Tool 🗂️

Flort is a powerful command-line tool designed to help developers create consolidated views of their project's source code. It generates comprehensive project overviews by combining directory trees, Python module outlines, and source file concatenation into a single, easily shareable output file.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)

## Features ✨

- **Directory Tree Generation**: Creates visual representation of project structure
- **Source File Concatenation**: Combines multiple source files into a single output
- **Python Module Outline**: Generates detailed outlines of Python modules including:
  - Function signatures with type hints
  - Class hierarchies
  - Docstrings
  - Decorators
- **Flexible File Filtering**:
  - Filter by file extensions
  - Include/exclude hidden files
  - Ignore specific directories
- **Configurable Output**: Choose between file output or console display

## Installation 🚀

```bash
pip install flort
```

## Quick Start 🏃‍♂️

Basic usage to analyze a Python project:

```bash
flort . --py --output=project_overview.txt
```

This will:
1. Scan the current directory for Python files
2. Generate a directory tree
3. Create a Python module outline
4. Concatenate all Python source files
5. Save everything to `project_overview.txt`

## Usage Examples 📚

### Basic Directory Analysis
```bash
# Analyze current directory, include only Python files
flort . --py

# Analyze multiple directories
flort src tests --py

# Include multiple file types
flort . --py --js --css
```

### Advanced Options
```bash
# Include hidden files
flort . --py --hidden

# Include all file types
flort . --all

# Output to console instead of file
flort . --py --output=stdio

# Skip directory tree generation
flort . --py --no-tree

# Generate only outline without source dump
flort . --py --outline --no-dump

# Ignore specific directories
flort . --py --ignore-dirs=venv,build
```

## Command Line Options 🎮

| Option | Description |
|--------|-------------|
| `DIRECTORY` | Directories to analyze (default: current directory) |
| `--output` | Output file path (default: `{current_dir}.flort`) |
| `--outline` | Generate Python module outline |
| `--no-dump` | Skip source file concatenation |
| `--no-tree` | Skip directory tree generation |
| `--all` | Include all file types |
| `--hidden` | Include hidden files |
| `--ignore-dirs` | Comma-separated list of directories to ignore |
| `--verbose` | Enable verbose logging |
| `--help` | Show help message |

## Output Format 📄

The generated output file follows this structure:

```
## Florted: 2025-01-02 05:54:57

## Directory Tree
|-- project/
|   |-- src/
|   |   |-- main.py
|   |-- tests/
|       |-- test_main.py

## Detailed Python Outline
### File: src/main.py
CLASS: MyClass
  DOCSTRING:
    Class description
  FUNCTION: my_method(arg1: str, arg2: int = 0) -> bool
    DOCSTRING:
      Method description

## File data
--- File: src/main.py
[source code here]
```

## Development 🛠️

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/yourusername/flort.git
cd flort

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install development dependencies
pip install -e ".[dev]"
```

### Running Tests

```bash
# Run all tests
python -m pytest

# Run with coverage report
python -m pytest --cov=flort tests/
```

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Code Style

- Follow PEP 8 guidelines
- Add type hints to function signatures
- Include docstrings for classes and functions
- Write unit tests for new features

## License 📝

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments 🙏

- Thanks to all contributors who have helped shape Flort
- Inspired by various code analysis and documentation tools in the Python ecosystem

## Support 💬

If you encounter any problems or have suggestions, please [open an issue](https://github.com/yourusername/flort/issues).
