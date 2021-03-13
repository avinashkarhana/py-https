import codecs
import os
from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")

setup(
    name="py-https",
    version=get_version("pyhttps/__init__.py"),
    author="Avinash Karhana",
    author_email="avinashkarhana1@gmail.com",
    description="A simple python https server",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/avinashkarhana/py-https",
    packages=find_packages(exclude="tests"),
    keywords=["https","pyhttps","https.server","pyhttps.server"], 
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)