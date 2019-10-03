#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_version(*file_paths):
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')

version = get_version('permabots', '__init__.py')

if sys.argv[-1] == 'publish':
    try:
        import wheel
    except ImportError:
        print('Wheel library missing. Please run "pip install wheel"')
        sys.exit()
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

if sys.argv[-1] == 'tag':
    print("Tagging the version on github:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='permabots',
    version='2.2.3',
    description="""Connect chats bots to your API apps""",
    long_description=readme + '\n\n' + history,
    author='Juan Madurga',
    author_email='jlmadurga@gmail.com',
    url='https://github.com/jlmadurga/permabots',
    packages=[
        'permabots',
    ],
    include_package_data=True,
    install_requires=[
        'django>=1.9.1',
        'celery==3.1.23',
        'djangorestframework==3.9.1',
        'python-telegram-bot==4.2.0',
        'Jinja2==2.8',
        'jinja2-time==0.1.0',
        'requests==2.10.0',
        'shortuuid==0.4.3',
        'kik==1.0.7',
        'messengerbot==0.1.4'
    ],
    license="BSD",
    zip_safe=False,
    keywords='permabots',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
