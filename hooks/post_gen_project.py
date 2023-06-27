import os

def remove_celery_files():
    file_names = [
        os.path.join("{{ cookiecutter.project_slug_snaked }}", "celery.py"),
    ]
    for file_name in file_names:
        os.remove(file_name)


def main():
    if "{{ cookiecutter.use_celery }}" == "n":
        remove_celery_files()


if __name__ == "__main__":
    main()
