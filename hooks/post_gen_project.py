import os
import shutil
import subprocess


def remove_drf_files():
    file_paths = [
        os.path.join("users", "forms.py"),
        os.path.join("users", "tests", "test_forms.py"),
    ]
    for file_path in file_paths:
        os.remove(file_path)

    dir_paths = [
        os.path.join("users", "api"),
    ]
    for dir_path in dir_paths:
        if os.path.exists(dir_path):
            shutil.rmtree(dir_path)

def remove_drf_packages():
    packages = [
        'dj-rest-auth',
        'django-cors-headers',
        'django-restql',
        'djangorestframework',
        'djangorestframework-simplejwt',
        'drf-yasg',
    ]
    file_path = os.path.join('pyproject.toml')

    with open(file_path, 'r') as file:
        lines = file.readlines()

    filtered_lines = lines
    for package in packages:
        filtered_lines = [line for line in filtered_lines if not line.startswith(package)]

    with open(file_path, 'w') as file:
        file.writelines(filtered_lines)

def remove_celery_files():
    file_paths = [
        os.path.join("{{ cookiecutter.project_slug_snaked }}", "celery.py"),
    ]
    for file_path in file_paths:
        os.remove(file_path)

def remove_celery_packages():
    packages = [
        'celery',
        'django-celery-beat',
        'django-celery-results',
        'django-redis',
    ]
    file_path = os.path.join('pyproject.toml')

    with open(file_path, 'r') as file:
        lines = file.readlines()

    filtered_lines = lines
    for package in packages:
        filtered_lines = [line for line in filtered_lines if not line.startswith(package)]

    with open(file_path, 'w') as file:
        file.writelines(filtered_lines)

def regenerate_peotry_lock_file():
    project_directory = os.getcwd()
    os.chdir(project_directory)
    subprocess.run(["poetry", "lock"])


def main():
    if "{{ cookiecutter.use_drf }}" == "n":
        remove_drf_files()
        remove_drf_packages()
        regenerate_peotry_lock_file()

    if "{{ cookiecutter.use_celery }}" == "n":
        remove_celery_files()
        remove_celery_packages()
        regenerate_peotry_lock_file()


if __name__ == "__main__":
    main()
