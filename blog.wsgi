import os
import sys

sys.path.append('/var/www/html/dj_blog/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'dj_blog.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
