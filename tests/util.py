import os

from sphinx.application import Sphinx
from io import StringIO

from conftest import KIDSFIRST_THEME_NAME


def build(src_dir, dest_dir, builder='html',  **kwargs):
    doctreedir = os.path.join(dest_dir, 'doctree/')

    status = StringIO()
    warning = StringIO()

    kwargs.update({
        'status': status,
        'warning': warning,
    })

    confoverrides = kwargs.pop('confoverrides', {})
    confoverrides['html_theme'] = KIDSFIRST_THEME_NAME
    kwargs['confoverrides'] = confoverrides

    app = Sphinx(src_dir, src_dir, dest_dir, doctreedir, builder, **kwargs)
    app.builder.build_all()

    return (app, status.getvalue(), warning.getvalue())
