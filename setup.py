#!/usr/bin/env python3

import os
import sys
import platform
from setuptools import setup, find_packages

def read(fname):
  return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
  name = "pat",
  version = "1.0",
  packages = [],
  scripts = ["scripts/pat"],
  install_requires = ["pillow>=2.7.0"],

  author = "Felix \"KoffeinFlummi\" Wiegand",
  author_email = "koffeinflummi@gmail.com",
  description = "Show images in your terminal.",
  long_description = read("README.md"),
  license = "MIT",
  keywords = "image images picture pictures terminal viewer",
  url = "https://github.com/KoffeinFlummi/pat",
  classifiers=[
    "Environment :: Console",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Topic :: Terminals :: Terminal Emulators/X Terminals",
    "Topic :: Utilities"
  ]
)
