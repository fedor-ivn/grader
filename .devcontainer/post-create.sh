#!/bin/bash

pip install --user -r .devcontainer/requirements.txt
pre-commit install --install-hooks
