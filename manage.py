#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from dotenv import find_dotenv, load_dotenv


def main():
    try:
        load_dotenv(find_dotenv(
                        filename='env/local.env',
                        raise_error_if_not_found=True
                    ))
    except OSError:
        load_dotenv(find_dotenv(filename='env/prod.env'))

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
