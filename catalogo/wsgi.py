import os
import sys
import pathlib

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
sys.path.insert(0, str(BASE_DIR / 'catalogo'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'catalogo.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
