import csv
import itertools
import os

from celery import chord
from celery.exceptions import Reject

from .app import app
from .core import gen_input_params, is_prime


def get_results_filename(max_num):
    return f"results/max_num={max_num}.csv"

def guesstimate_optimal_chunk_size(matrix_row_size):
    # Each worker will bite at several matrix rows at once, depending on how greedy our algo is
    return int(matrix_row_size * app.conf.PDAJ_WORKER_GREED_FACTOR)

@app.task(ignore_result=True)
def seed_computations(max_num):
    results_filename = get_results_filename(max_num)
    if os.path.exists(get_results_filename(max_num)):
        raise Reject(f"Computations for '{results_filename}' have already been seeded!")

    # create the results file, to mark that computations have been seeded
    open(results_filename, 'w').close()

    from celery import chunks
    chord(
        compute_prime_matrix_element.chunks(
            ((x, y, num) for x, y, num in gen_input_params(max_num)),
            guesstimate_optimal_chunk_size(max_num),
        ).group(),
        store_prime_matrix.s(max_num)
    ).delay()

@app.task
def compute_prime_matrix_element(x, y, num):
    return x, y, num, is_prime(num)

@app.task
def store_prime_matrix(results, max_num):
    results_filename = get_results_filename(max_num)
    with open(results_filename, 'w') as out:
        report = csv.writer(out)
        # results need to be de-chunked before use, which can be done by "flattening" their Python iterator
        for x, y, num, is_prime in itertools.chain.from_iterable(results):
            report.writerow((x, y, num, int(is_prime)))

        return results_filename
