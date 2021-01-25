from celery import Celery
from celery.signals import worker_ready


app = Celery('distributed')
app.config_from_object('distributed.settings')

@worker_ready.connect
def bootstrap(**kwargs):
    from .tasks import seed_computations

    delay_time = 3 # seconds
    print(f"Getting ready to automatically seed computations in {delay_time} seconds...")
    seed_computations.apply_async(
        kwargs={
            'max_num': app.conf.PDAJ_MAX_NUM,
        },
        countdown=delay_time,
    )
