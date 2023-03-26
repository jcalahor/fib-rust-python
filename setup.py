
import pathlib

from setuptools import find_packages, setup


with open("README.md", "r") as fh:
    long_description = fh.read()
    

setup(
    name="fib_rust_python",
    version="",
    author="Jaime Calahorrano based on the work of Maxwell Flitton",
    author_email="jcalahor@yahoo.com",
    description="Calculates a Fibonacci number",
    long_description="A basic library that \
    calculates Fibonacci numbers",
    long_description_content_type="text/markdown",
    url="https://github.com/jcalahor/fib-rust-python.git",
    install_requires=[
        "PyYAML>=4.1.2",
        "dill>=0.2.8"
    ],
    extras_require={
     'server': ["Flask>=1.0.0"]
    },    packages=find_packages(exclude=("tests",)),
    classifiers=[
    "Development Status :: 4 - Beta",
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
    ],
    python_requires='>=3',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'fib-number = fib_rust_python.cmd.fib_numb:fib_numb',
        ],  
    },
)


