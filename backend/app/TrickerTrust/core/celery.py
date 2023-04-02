import os
from os import getenv
from celery import Celery

redis_password = getenv("REDIS_PASSWORD")
redis_host = getenv("REDIS_HOST")
redis_database = getenv("REDIS_DATABASE")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
redis_url = f"redis://:{redis_password}@{redis_host}/{redis_database}"
app = Celery("core", broker=redis_url, backend=redis_url)
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.add_periodic_task(3600 * 3, app.signature("currency_course.tasks.update_course"))
