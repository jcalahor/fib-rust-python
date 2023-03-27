#!/usr/bin/env python
from setuptools import dist
dist.Distribution().fetch_build_eggs(['setuptools_rust'])
from setuptools import setup
from setuptools_rust import Binding, RustExtension


setup(
    name="fib-rust-python",
    version="",
    rust_extensions=[RustExtension(
        ".fib_rust_python.fib_rust_python",
        path="Cargo.toml", binding=Binding.PyO3)],
    author="Jaime Calahorrano based on the work of Maxwell Flitton",
    packages=["fib_rust_python"],
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
            "License :: OSI Approved :: MIT License",
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Programming Language :: Python",
            "Programming Language :: Rust",
            "Operating System :: POSIX",
            "Operating System :: MacOS :: MacOS X",
        ],
    zip_safe=False,
    python_requires='>=3',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'fib-number = fib_rust_python.cmd.fib_numb:fib_numb',
        ],  
    },
)


