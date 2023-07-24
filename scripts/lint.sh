#!/usr/bin/env bash

set -x

mypy src
black src --check
isort --check-only app
flake8
