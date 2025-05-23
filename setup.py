from setuptools import setup, find_packages

setup(
    name='flort',
    version='0.1.10.2',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'flort = flort.wrapper:main'  # Changed to use the wrapper
        ]
    },
    install_requires=[
        'argparse',
        'pathlib',  
        'datetime', 
        'logging',  
        'windows-curses;platform_system=="Windows"',  # Only on Windows, standard on Unix/Linux
      ],
    author='Chris Watkins',
    author_email='chris@watkinslabs.com',
    description='A utility to flatten your source code directory into a single file for LLM usage',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/chris17453/flort',
    classifiers=[
     'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    keywords='source code, concatenation, project overview, documentation',
)