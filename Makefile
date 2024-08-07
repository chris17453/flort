.PHONY: build tests clean setup

# Remove previous build artifacts
clean:
	rm -rf ./dist/*
	rm -rf *.egg-info

# Build the package and upload to PyPI
build: clean
	python setup.py sdist

upload: build
	twine upload dist/*

# Set up the test environment
setup:
	chmod +x tests/setup.sh
	bash tests/setup.sh

# Build the package and then run tests
test: setup build
	pytest tests/test_cli.py
