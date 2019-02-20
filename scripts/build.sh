#!/bin/bash

# abort on any non-zero exit code
set -e

python3 -m venv venv
. venv/bin/activate
pip install -e .
pip install -r dev-requirements.txt
