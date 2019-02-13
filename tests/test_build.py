import os

import pytest

from sphinx import addnodes

from util import build
from conftest import (
    SPHINX_BUILDER_NAMES,
    KIDSFIRST_CSS_FILE
)


@pytest.mark.parametrize('builder_name',
                         SPHINX_BUILDER_NAMES
                         )
def test(builder_name, data_dir, tmpdir):
    src_dir = os.path.join(data_dir, 'basic', 'source')
    dest_dir = tmpdir.mkdir('build')

    # Build worked
    app, status, warning = build(src_dir, dest_dir)

    # Check Table of contents tree
    assert app.env.get_doctree('index').traverse(addnodes.toctree)

    with open(os.path.join(app.outdir, 'index.html')) as index_file:
        content = index_file.read()

    # Kids First css file exists
    assert os.path.isfile(os.path.join(dest_dir,
                                       '_static', 'css', KIDSFIRST_CSS_FILE))
    # Kids First css is referenced
    assert ('<link rel="stylesheet" '
            'href="_static/css/kidsfirst.css" type="text/css" />') in content
