from setuptools import setup, find_packages

setup(
    name="OpenCyb3r",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "flask"
    ],
    entry_points={
        "console_scripts": [
            "opencyb3r=main:main",
        ],
    },
    author="Daniel Sinatra",
    description="A cybersecurity tool suite",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)