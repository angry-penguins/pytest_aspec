SHELL := /bin/bash
.PHONY: help

help:  ## help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

setup:  ## sets up your local venv for contribution
	@if which python3.11 && [ ! -f .venv/bin/activate ] ; then python3.11 -m venv .venv ; fi
	@if which python3.10 && [ ! -f .venv/bin/activate ] ; then python3.10 -m venv .venv ; fi
	@source .venv/bin/activate \
	  && pip install -r requirements-dev.txt

test:   ## runs tests via pytest
	@source .venv/bin/activate \
	  && py.test -x tests/ --cov pytest_aspec --cov-report term-missing

lint:  ## Run static code checks
	@source .venv/bin/activate \
  	&& isort --check pytest_aspec tests \
	  && flake8 .

clean:  ## Clean cache and temporary files
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@rm -rf *.egg-info
