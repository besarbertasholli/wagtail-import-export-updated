#!/usr/bin/env python

from setuptools import setup, find_packages
from wagtailimportexport import __version__

setup(
    name="wagtail-import-export-updated",
    version=__version__,
    description="Import/Export for Wagtail CMS pages, images and documents.",
    author="Besarber Tasholli",
    author_email="besarbertasholli@hotmail.com",
    url="https://github.com/besarbertasholli/wagtail-import-export-updated",
    packages=find_packages(),
    include_package_data=True,
    license="BSD",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Framework :: Django",
    ],
)
