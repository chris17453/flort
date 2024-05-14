.PHONY: build test

build:
	rm -f ./dist/*
	python setup.py sdist
	twine upload dist/*

test:
	pytest tests/test_cli.py	
