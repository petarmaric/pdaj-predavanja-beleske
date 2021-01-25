from multiprocessing import cpu_count

from decouple import config


# Task settings

task_compression = 'bzip2'


# Task execution settings

task_track_started = True

task_acks_late = True

task_reject_on_worker_lost = True


# Results backend settings

result_backend = config('CELERY_RESULT_BACKEND', default='redis://redis:6379/0')

result_backend_transport_options = {
    # Preserve order of Celery chord/group results
    # See https://docs.celeryproject.org/en/stable/getting-started/brokers/redis.html#group-result-ordering
    'result_chord_ordered': True,

    'result_compression': task_compression,
}

result_expires = None


# Broker settings

broker_url = config('CELERY_BROKER_URL', default='redis://redis:6379/0')


# Worker settings

imports = [
    'distributed.tasks',
]

worker_concurrency = config('CELERY_WORKER_CONCURRENCY', default=0, cast=int)
if worker_concurrency == 0: # auto-detect number of CPU cores
    worker_concurrency = cpu_count()

worker_max_memory_per_child = 2 * 1024**2 # in KBs


# PDAJ app settings

PDAJ_MAX_NUM = config('PDAJ_MAX_NUM', default=3000, cast=int)

PDAJ_WORKER_GREED_FACTOR = config('PDAJ_WORKER_GREED_FACTOR', default=10.0, cast=float)
