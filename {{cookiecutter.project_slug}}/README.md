# {{ cookiecutter.project_description }}

This repository is used for the backend of the {{ cookiecutter.project_description }} App developed using Django.

## Local Environment Setup

### Required Installations

1. [Python 3.10](https://www.python.org/downloads/)  
    On macOS (with Homebrew): `brew install python3`
2. [Poetry 1.1.11](https://python-poetry.org/docs/#installation)  
    `curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -`
3. [PostgreSQL 14.0](https://www.postgresql.org/download/)  
    On macOS (with Homebrew): `brew install postgres`

### Install Requirements

1. `poetry install`  
    This installs the libraries required for this project
2. `pre-commit install` 
    This installs pre-commit hooks to enforce code style.

### Setup PostgreSQL Database

```bash
sudo -u postgres psql

CREATE USER {{ cookiecutter.project_slug }} WITH PASSWORD '{{ cookiecutter.project_slug }}';
ALTER USER {{ cookiecutter.project_slug }} CREATEDB;

CREATE DATABASE {{ cookiecutter.project_slug }} owner {{ cookiecutter.project_slug }};
```

### Configure .env File

1. Copy `.env.example` to `.env` and customize its values.
2. `SECRET_KEY` should be a random string, you can generate a new one using the following command:  
    `python -c 'from secrets import token_urlsafe; print("SECRET_KEY=" + token_urlsafe(50))'`
3. Set `DATABASE_URL` to `POSTGRES_URL=postgres://{{ cookiecutter.project_slug }}:{{ cookiecutter.project_slug }}@localhost/{{ cookiecutter.project_slug }}`.

### Setup DB Schema

1. `./manage.py migrate`  
    This applies the migrations to your database
2. `./manage.py createsuperuser`  
    This creates your superuser account. Just follow the prompts.

## Running the App

1. `poetry shell`  
    If it's activated you'll see the virtual environment name at the beginning of your prompt, something like `("{{ cookiecutter.project_slug }}"-2wVcCnjv-py3.10)`.
2. `./manage.py runserver`

## Running the Tests

1. `poetry shell`
2. `pytest`  
    Run `pytest --cov=. --cov-report term-missing` to also show coverage report.

# FAQs

1. Changing the `.env` file variables has no effect.  
    Run `export $(grep -v '^#' .env | xargs -0)` to source the file  
    or  
    Exit shell and run `poetry shell` again to reload the env file
