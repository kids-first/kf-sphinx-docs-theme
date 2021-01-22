# -*- coding: utf-8 -*-
import os
from setuptools import setup
from sphinx_kidsfirst_theme import __version__

root_dir = os.path.dirname(os.path.abspath(__file__))
req_file = os.path.join(root_dir, 'requirements.txt')
with open(req_file) as f:
    requirements = f.read().splitlines()

setup(
    name='sphinx_kidsfirst_theme',
    version=__version__,
    description='Kids First Read the Docs inspired theme for Sphinx',
    zip_safe=False,
    packages=['sphinx_kidsfirst_theme'],
    package_data={'sphinx_kidsfirst_theme': [
        'theme.conf',
        'layout.html',
        'static/css/*.css'
    ]},
    include_package_data=True,
    # See http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package
    entry_points={
        'sphinx.html_themes': [
            'sphinx_kidsfirst_theme = sphinx_kidsfirst_theme',
        ]
    },
    install_requires=requirements
)
