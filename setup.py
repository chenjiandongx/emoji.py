# coding=utf-8

from setuptools import setup, find_packages

# RELEASE STEPS
# $ python setup.py bdist_wheel
# $ python twine upload dist/VX.Y.Z.whl
# $ git tag -a VX.Y.Z -m "release version VX.Y.Z"
# $ git push origin VX.Y.Z

NAME = "emoji.py"
VERSION = "0.1.0"
URL = "https://github.com/chenjiandongx/emoji.py"
AUTHOR = "chenjiandongx"
AUTHOR_EMAIL = "chenjiandongx@qq.com"
LICENSE = "MIT"
REQUIRES = ["pyperclip", "pick", "fuzzywuzzy"]
MODULES = ["emoji"]
DESC = "Search emoji via command-line"

setup(
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    name=NAME,
    version=VERSION,
    license=LICENSE,
    install_requires=REQUIRES,
    url=URL,
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    py_modules=MODULES,
    description=DESC,
    entry_points={"console_scripts": ["emoji=emoji:command_line_runner"]},
)
