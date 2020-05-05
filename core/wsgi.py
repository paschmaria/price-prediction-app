"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dotenv import find_dotenv, load_dotenv

try:
    load_dotenv(find_dotenv(
                    filename='env/local.env',
                    raise_error_if_not_found=True
                ))
except OSError:
    load_dotenv(find_dotenv(filename='env/prod.env'))


application = get_wsgi_application()
