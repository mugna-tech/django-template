import os
import shutil


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


def remove_celery_files():
    file_paths = [
        os.path.join("{{ cookiecutter.project_slug_snaked }}", "celery.py"),
    ]
    for file_path in file_paths:
        os.remove(file_path)


def main():
    if "{{ cookiecutter.use_drf }}" == "n":
        remove_drf_files()

    if "{{ cookiecutter.use_celery }}" == "n":
        remove_celery_files()


if __name__ == "__main__":
    main()
