SHELL := /bin/bash

# Install runtime dependencies
init:
	pip --disable-pip-version-check --no-cache-dir install --upgrade -r requirements.txt

init-dev: init
	pip --disable-pip-version-check --no-cache-dir install --upgrade -r .devcontainer/dev-requirements.txt
