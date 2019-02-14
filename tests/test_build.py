import os

import pytest

from sphinx import addnodes

from util import build
from conftest import SPHINX_BUILDER_NAMES


@pytest.mark.parametrize('builder_name',
                         SPHINX_BUILDER_NAMES
                         )
def test(builder_name, data_dir, tmpdir):
    src_dir = os.path.join(data_dir, 'basic', 'source')
    dest_dir = os.path.join(data_dir, 'basic', 'build')

    # Build worked
    app, status, warning = build(src_dir, dest_dir)

    # Check Table of contents tree
    assert app.env.get_doctree('index').traverse(addnodes.toctree)

    with open(os.path.join(app.outdir, 'index.html')) as index_file:
        content = index_file.read()

    # Kids First css is referenced
    kf_css_element = (
        '<link rel="stylesheet" href="https://kids-first.github.io/'
        'kf-sphinx-docs-theme/sphinx_kidsfirst_theme/static/css/'
        'kidsfirst.css" type="text/css" />'
    )

    assert kf_css_element in content
