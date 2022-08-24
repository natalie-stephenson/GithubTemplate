import pathlib

import setuptools

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setuptools.setup(
    name="project_name", # Update
    version="0.0.0",
    description="[insert description here]", # Update
    long_description=README,
    packages=[
        "project_name", # Update
    ],
    author="KPMGUK",
    author_email="many@kpmg.co.uk",
    long_description_content_type="text/markdown",
    url="" # Update with github URL e.g. "https://github.com/KPMG-UK/project_name"
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Development Status :: 4 - Beta",
    ],
    python_requires=">=3.9",
    install_requires=[
        "pandas>=1.3.1",
        "pytest>=6.2.4",
    ],
)
