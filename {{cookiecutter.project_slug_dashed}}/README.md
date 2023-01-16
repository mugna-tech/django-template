# {{ cookiecutter.project_name }}

This repository is used for the backend of the {{ cookiecutter.project_name }} App developed using Django.

## Docker Setup
To run this project in a Docker it is assumed you have a setup [Docker Compose](https://docs.docker.com/compose/).

**Install Docker:**
   - Linux - [get.docker.com](https://get.docker.com/)
   - Windows or MacOS - [Docker Desktop](https://www.docker.com/products/docker-desktop)

1. Open CLI and CD to project root.
2. Clone this repo and `git clone git@github.com:mugna-tech/{{ cookiecutter.project_slug_dashed }}.git`
3. Go to project folder where manage.py is located. 
4. Execute `docker-compose up --build` This will build the docker container.
5. `docker exec -it {{ cookiecutter.project_slug_snaked }}_web python manage.py migrate`
6. `docker exec -it {{ cookiecutter.project_slug_snaked }}_web python manage.py createsuperuser`

### Docker Notes:
You will only execute `docker-compose up --build` if you have changes in your Dockerfile. To start docker containers you can either use `docker-compose up` or `docker-compose start`

**Docker Django Environments**
1. To add or use different environment values copy `docker-compose.override.yml.example` and rename it to `docker-compose.override.yml`
and change or add environment variables needed.
2. Add a `.env` file in your project root. 

Any changes in the environment variable will need to re-execute the `docker-compose up`

**To add package to poetry**
```sh
docker exec -it {{ cookiecutter.project_slug_snaked }}_web poetry config virtualenvs.create false
docker exec -it {{ cookiecutter.project_slug_snaked }}_web poetry add new_package_name
```

**Example of executing Django manage.py commands**
```sh
docker exec -it {{ cookiecutter.project_slug_snaked }}_web python manage.py shell
docker exec -it {{ cookiecutter.project_slug_snaked }}_web python manage.py makemigrations
docker exec -it {{ cookiecutter.project_slug_snaked }}_web python manage.py loaddata appname
```

**To copy site-packages installed by poetry from docker to your host machine**
```sh
docker cp {{ cookiecutter.project_slug_snaked }}_web:/usr/local/lib/python3.11/site-packages <path where you want to store the copy>
```

**DEBUG NOTES:**
1. When adding PDB to your code you can interact with it in your CLI by executing `docker start -i {{ cookiecutter.project_slug_snaked }}_web`.
2. If you experience this error in web docker container `port 5432 failed: FATAL:  the database system is starting up` -- automatically force restart the {{ cookiecutter.project_slug_snaked }}_web docker container by executing.
```sh
docker restart {{ cookiecutter.project_slug_snaked }}_web
```

## Local Environment Setup

### Required Installations

1. [Python 3.11](https://www.python.org/downloads/)  
    On macOS (with Homebrew): `brew install python3`
2. [Poetry 1.1.11](https://python-poetry.org/docs/#installation)  
    `curl -sSL https://install.python-poetry.org | python3 -`
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

CREATE USER {{ cookiecutter.project_slug_snaked }} WITH PASSWORD '{{ cookiecutter.project_slug_snaked }}';
ALTER USER {{ cookiecutter.project_slug_snaked }} CREATEDB;

CREATE DATABASE {{ cookiecutter.project_slug_snaked }} owner {{ cookiecutter.project_slug_snaked }};
```

### Configure .env File

1. Copy `.env.example` to `.env` and customize its values.
2. `SECRET_KEY` should be a random string, you can generate a new one using the following command:  
    `python -c 'from secrets import token_urlsafe; print("SECRET_KEY=" + token_urlsafe(50))'`
3. Set `DATABASE_URL` to `POSTGRES_URL=postgres://{{ cookiecutter.project_slug_snaked }}:{{ cookiecutter.project_slug_snaked }}@localhost/{{ cookiecutter.project_slug_snaked }}`.

### Setup DB Schema

1. `./manage.py migrate`  
    This applies the migrations to your database
2. `./manage.py createsuperuser`  
    This creates your superuser account. Just follow the prompts.

## Running the App

1. `poetry shell`  
    If it's activated you'll see the virtual environment name at the beginning of your prompt, something like `("{{ cookiecutter.project_slug_snaked }}"-2wVcCnjv-py3.11)`.
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
