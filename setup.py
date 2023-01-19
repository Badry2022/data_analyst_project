"""Python setup.py for data_analyst_project package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("data_analyst_project", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="data_analyst_project",
    version=read("data_analyst_project", "VERSION"),
    description="Awesome data_analyst_project created by Badry2022",
    url="https://github.com/Badry2022/data_analyst_project/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Badry2022",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["data_analyst_project = data_analyst_project.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
