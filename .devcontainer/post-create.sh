#!/bin/bash

pip install --user -r .devcontainer/requirements.txt
pre-commit install --install-hooks
TOKEI_DOWNLOAD_URL="https://github.com/XAMPPRocky/tokei/releases/latest/download/tokei-x86_64-unknown-linux-gnu.tar.gz"
sudo wget -qO - $TOKEI_DOWNLOAD_URL | sudo tar xfz - -C /usr/local/bin
