"""
WSGI config for biblioteka project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os, sys

sys.path.append('/home/strzepcz/biblioteka')
sys.path.append('/home/strzepcz/biblioteka/env/lib/python3.5/site-packages')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "biblioteka.settings")

application = get_wsgi_application()
