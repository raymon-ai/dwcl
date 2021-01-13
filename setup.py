import json
import os
from setuptools import setup


with open("package.json") as f:
    package = json.load(f)

with open("README.md") as f:
    long_description = f.read()

package_name = package["name"].replace(" ", "_").replace("-", "_")

setup(
    name=package_name,
    version=package["version"],
    author=package["author"],
    url="https://github.com/raymon-ai/dwcl",
    packages=[package_name],
    include_package_data=True,
    license=package["license"],
    description=package.get("description", package_name),
    install_requires=[],
    classifiers=["Framework :: Dash",],
    long_description=long_description,
    long_description_content_type="text/markdown",
)
