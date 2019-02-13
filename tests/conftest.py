import os
import pytest

KIDSFIRST_THEME_NAME = 'sphinx_kidsfirst_theme'
KIDSFIRST_CSS_FILE = 'kidsfirst.css'
SPHINX_BUILDER_NAMES = ['html', 'singlehtml']


@pytest.fixture(scope='function')
def data_dir():
    return os.path.join((os.path.dirname(__file__)), 'data')
