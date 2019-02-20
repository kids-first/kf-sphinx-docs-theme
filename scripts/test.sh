#!/bin/bash

# abort on any non-zero exit code
set -e

. venv/bin/activate
py.test tests
