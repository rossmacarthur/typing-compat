"""
Setup file for typing-compat.
"""

import io
import os
import re

from setuptools import setup


def get_metadata():
    """
    Return metadata for typing-compat.
    """
    here = os.path.abspath(os.path.dirname(__file__))
    init_path = os.path.join(here, 'typing_compat.py')
    readme_path = os.path.join(here, 'README.md')

    with io.open(init_path, encoding='utf-8') as f:
        about_text = f.read()

    metadata = {
        key: re.search(r'__' + key + r"__ = '(.*?)'", about_text).group(1)
        for key in ('title', 'version', 'url', 'author', 'author_email', 'description')
    }
    metadata['name'] = metadata.pop('title')

    with io.open(readme_path, encoding='utf-8') as f:
        metadata['long_description'] = f.read()
        metadata['long_description_content_type'] = 'text/markdown'

    return metadata


metadata = get_metadata()

setup(
    # Options
    install_requires=['typing; python_version<"3.5"'],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
    py_modules=['typing_compat'],
    # Metadata
    download_url='{url}/archive/{version}.tar.gz'.format(**metadata),
    project_urls={'Issue Tracker': '{url}/issues'.format(**metadata)},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    **metadata
)
