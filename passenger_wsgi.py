# passenger_wsgi.py
import sys
import os

# Add your python path if needed
INTERP = os.path.expanduser("/usr/local/bin/python3.8")
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

from app import app as application
