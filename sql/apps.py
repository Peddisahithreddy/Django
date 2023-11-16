from django.apps import AppConfig
from sql.sql.models import Admin
import sys
sys.path.append('/Face_recognizer_frontend/users.py')



class SqlConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sql'
