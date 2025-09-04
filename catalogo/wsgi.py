"""
WSGI config for catalogo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'catalogo.settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'catalogo.settings')
import os
import sys
import pathlib
BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
sys.path.insert(0, str(BASE_DIR / 'catalogo'))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'catalogo.settings')

application = get_wsgi_application()
