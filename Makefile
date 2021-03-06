.DEFAULT_GOAL := default_target
.PHONY: default_target lint test clean

db := $(DATABASE_URL)
url := $(POSTMAN_URL)
url_security := $(SECURITY_URL)
stress_url := $(STRESS_TEST_URL)
export FLASK_APP=migrate.py


clean:
	@rm -fr reports/
	@mkdir reports


setup-dev:
	pip install -r requirements-dev.txt


test:
	py.test -v


test-cov:
	py.test -v --cov-report=term  --cov-report=html --cov=controller


code-convention:
	flake8
	pycodestyle


## database

.PHONY: db_up
db_up:
	flask db upgrade

.PHONY: db_down
db_down:
	flask db downgrade

.PHONY: db_autogenerate
db_autogenerate:
	flask db revision --autogenerate

.PHONY: db_migrate
db_migrate:
	flask db migrate


run_server:
	python -m wsgi


default_target: clean code-convention test

