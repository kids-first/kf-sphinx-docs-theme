<p align="center">
  <img src="docs/images/logo.svg" alt="Kids First Data Ingest Library" width="660px">
</p>
<p align="center">
  <a href="https://github.com/kids-first/kf-sphinx-docs-theme/blob/master/LICENSE"><img src="https://img.shields.io/github/license/kids-first/kf-sphinx-docs-theme.svg?style=for-the-badge"></a>
  <a href="https://circleci.com/gh/kids-first/kf-sphinx-docs-theme"><img src="https://img.shields.io/circleci/project/github/kids-first/kf-sphinx-docs-theme.svg?style=for-the-badge"></a>
</p>

Kids First Sphinx Docs Theme
=============================

A Sphinx theme that inherits the Sphinx Read the Docs theme https://github.com/rtfd/sphinx_rtd_theme and adds Kids First styling on top of it.

Sphinx is a web documentation generator for Python applications

# Users

## Installation
```
pip install -e git+https://github.com/kids-first/kf-sphinx-docs-theme.git#egg=kf-sphinx-docs-theme
```

To use the Kids First Sphinx theme simply put the following in your Sphinx configuration file
(conf.py).
```
html_theme = 'sphinx_kidsfirst_theme'
```
See http://www.sphinx-doc.org/en/master/usage/quickstart.html
for information on how to use Sphinx and what `conf.py` is.

# Developers
For information on creating Sphinx themes see: http://www.sphinx-doc.org/en/stable/theming.html#creating-themes

## Test
```
# Install reqs
pip install -r dev-requirements.txt

# Run tests
python -m pytest tests
```
