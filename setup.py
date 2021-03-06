import os

from setuptools import setup

if os.environ.get("distutils_issue8876_workaround_enabled", False):
    # sdist_hack: Remove reference to os.link to disable using hardlinks when
    #             building setup.py's sdist target.  This is done because
    #             VirtualBox VMs shared filesystems don't support hardlinks.
    del os.link

NAME = "entrypoint2"
URL = "https://github.com/ponty/entrypoint2"
DESCRIPTION = (
    "easy to use command-line interface for python modules, fork of entrypoint"
)
PACKAGES = [
    NAME,
    NAME + ".examples",
]

# get __version__
__version__ = None
exec(open(os.path.join(NAME, "about.py")).read())
VERSION = __version__

# extra = {}
# if sys.version_info >= (3,):
#     extra['use_2to3'] = True

classifiers = [
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    "License :: OSI Approved :: BSD License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
]

install_requires = ["argparse"]

# compatible with distutils of python 2.3+ or later
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=open("README.rst", "r").read(),
    classifiers=classifiers,
    keywords="argparse decorator optparse signature command-line",
    author="ponty",
    # author_email='',
    url=URL,
    license="BSD",
    packages=PACKAGES,
    # include_package_data=True,
    # zip_safe=False,
    install_requires=install_requires,
    # **extra
)
