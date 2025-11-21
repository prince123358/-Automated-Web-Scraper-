from .celery_app import celery
from datetime import timedelta


# example schedule: run `scrape_and_store` every 15 minutes for a list of URLs
celery.conf.beat_schedule = {
'scrape-every-15-mins': {
'task': 'tasks.tasks.scrape_and_store',
'schedule': timedelta(minutes=15),
'args': ('https://example.com/target-page',),
},
}
