import os
from celery import Celery
from dotenv import load_dotenv


load_dotenv()


REDIS_URL = os.getenv('REDIS_URL', 'redis://redis:6379/0')


celery = Celery(
'scraper_tasks',
broker=REDIS_URL,
backend=REDIS_URL,
)


# optional: celery config
celery.conf.update(
result_expires=3600,
task_serializer='json',
accept_content=['json'],
)
