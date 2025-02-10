# Flort: File Concatenation and Project Overview Tool 🗂️

Flort is a powerful command-line tool designed to help developers create consolidated views of their project's source code. It generates comprehensive project overviews by combining directory trees, Python module outlines, and source file concatenation into a single, easily shareable output file.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)

## Features ✨

- **Interactive File Selection UI**: Optional terminal-based interface for intuitive file and directory selection
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
  - Include specific files
- **Configurable Output**: Choose between file output or console display

## Installation 🚀

```bash
pip install flort
```

## Quick Start 🏃‍♂️

Using command line:
```bash
# Basic usage with Python files
flort . --py

# Using interactive UI
flort --ui --py
```

## Usage Examples 📚

### Standard Command Line Usage
```bash
# Basic directory analysis with Python files
flort . --py

# Multiple directories and file types
flort src tests --py --js --css

# Include specific files and ignore directories
flort . --py --include-files=setup.py,README.md --ignore-dirs=venv,build

# Output to console with hidden files
flort . --all --hidden --output=stdio

# Python outline only, no source dump
flort . --py --outline --no-dump

# Complex configuration
flort src tests \
    --py --js \
    --ignore-dirs=venv,build \
    --include-files=setup.py \
    --hidden \
    --output=project.txt
```

### Interactive UI Usage (Optional)
The `--ui` flag enables an interactive terminal interface for file selection:

```bash
# Basic UI launch
flort --ui

# UI with preselected Python files
flort --ui --py

# UI with included files and no output file
flort --ui --include-files=setup.py,requirements.txt --output=stdio

# UI with multiple extensions and specific directories
flort --ui --py --js --css src tests

# UI with all extensions and hidden files
flort --ui --all --hidden

# UI with outline only, no source dump
flort --ui --outline --no-dump --py

# UI with full configuration
flort --ui \
    --py --js \
    --ignore-dirs=venv,build \
    --include-files=setup.py \
    --hidden \
    --output=project.txt \
    src tests
```

## Command Line Options 🎮

| Option | Description |
|--------|-------------|
| `--ui` | Launch interactive file selector interface |
| `DIRECTORY` | Directories to analyze (default: current directory) |
| `--output` | Output file path (default: `{current_dir}.flort`) |
| `--outline` | Generate Python module outline |
| `--no-dump` | Skip source file concatenation |
| `--no-tree` | Skip directory tree generation |
| `--all` | Include all file types |
| `--hidden` | Include hidden files |
| `--ignore-dirs` | Comma-separated list of directories to ignore |
| `--include-files` | Comma-separated list of files to include |
| `--verbose` | Enable verbose logging |
| `--help` | Show help message |

## Interactive UI Controls 🎮

| Key | Action |
|-----|--------|
| ↑/↓ | Navigate files/directories |
| ←/→ | Navigate directory tree |
| SPACE | Toggle selection |
| i | Toggle ignore |
| f | Edit file type filters |
| v | View selected/ignored items |
| q | Save and exit |
| ESC | Exit without saving |

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
git clone https://github.com/chris17453/flort.git
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

This project is licensed under the BSD 3 License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments 🙏

- Thanks to all contributors who have helped shape Flort
- Inspired by various code analysis and documentation tools in the Python ecosystem

## Support 💬

If you encounter any problems or have suggestions, please [open an issue](https://github.com/chris17453/flort/issues).