# Django Template

A Django template to jumpstart your Django projects using cookiecutter. [Cookiecutter](https://github.com/cookiecutter/cookiecutter).  

## Features

- Always `up-to-date` with the help of [`@dependabot`](https://dependabot.com/)
- [`poetry`](https://github.com/python-poetry/poetry) for managing dependencies
- Supports latest `python` 3.11+
- Latest `Django` 4.2+
- [12-Factor](https://www.12factor.net/) based settings using [`django-environ`](https://github.com/joke2k/django-environ)
- [`django-celery`](https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html) for background and periodic tasks (**optional)
- Authentication via [`django-allauth`](https://github.com/pennersr/django-allauth)
- [`django-rest-framework`](https://github.com/encode/django-rest-framework) for building Web APIs (**optional)
- GraphQL like API using [`restql`](https://github.com/yezyilomo/django-restql) (**optional)
- Token Authentication using [`simplejwt`](https://github.com/jazzband/djangorestframework-simplejwt) (**optional)
- API Authentication Endpoints via [`dj-rest-auth`](https://github.com/iMerica/dj-rest-auth) (**optional)
- API documentation via [`drf-yasg`](https://github.com/axnsan12/drf-yasg) (**optional)
- Renders Django projects with 100% starting test [`coverage`](https://github.com/nedbat/coveragepy)
- [`pytest`](https://pytest.org/) for unit tests
- [`factory-boy`](https://github.com/FactoryBoy/factory_boy) for test fixtures
- Serve static files with [`whitenoise`](https://whitenoise.readthedocs.io/)
- Default integration with [`pre-commit`](https://github.com/pre-commit/pre-commit) for identifying simple issues before submission to code review
  - [`isort`](https://github.com/timothycrosley/isort) for sorting imports
  - [`black`](https://github.com/psf/black) and [`flake8`](https://gitlab.com/pycqa/flake8) for coding style and standards

## Usage

### Required Installations

First, install the [dependencies](https://cookiecutter.readthedocs.io/en/latest/).
```bash
pip install cookiecutter
```

Then run it against this repo:
```bash
cookiecutter https://github.com/mugna-tech/django-template
```

Answer the prompts with your own desired options. For example:
```bash
project_name [Mugna]: Mugna Tech
project_slug [mugna_tech]: mugna
```

A new directory will be created with your project slug as the name.
