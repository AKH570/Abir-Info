#this is for local passenger
import os
import sys
from Abir.wsgi import application

sys.path.insert(0, os.path.dirname(__file__))

environ = os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Abir.settings")