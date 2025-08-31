# alx_travel_app_0x03/alx_travel_app_0x03/celery.py
import os
from celery import Celery

# set default Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alx_travel_app_0x03.settings')

app = Celery('alx_travel_app_0x03')

# load settings from Django settings, namespace CELERY_
app.config_from_object('django.conf:settings', namespace='CELERY')

# discover tasks in each app
app.autodiscover_tasks()
