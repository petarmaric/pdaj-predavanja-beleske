import csv
import fnmatch
import itertools
import os


def debug_stream(stream, start=0, stop=None):
    for item in itertools.islice(stream, start, stop):
        print(item)

def find_files(top_dir='.'):
    for dirpath, _, filenames in os.walk(top_dir):
        for name in filenames:
            yield os.path.join(dirpath, name)

def filter_filenames_by_pattern(filenames, pattern):
    for name in filenames:
        if fnmatch.fnmatchcase(name, pattern):
            yield name

def parse_files(filenames):
    for name in filenames:
        with open(name) as fp:
            for line in fp:
                yield line.strip()

def find_student(lines, student_name):
    for line in lines:
        if student_name in line:
            yield line

def pipeline(top_dir):
    filenames = find_files(top_dir)
    filenames = filter_filenames_by_pattern(filenames, '*.csv')
    filenames = filter_filenames_by_pattern(filenames, '*T34*')

    lines = parse_files(filenames)
    lines = find_student(lines, 'Ognjen')

    return lines


def main():
    stream = pipeline(top_dir='/mnt')
    debug_stream(stream, start=0, stop=None)

if __name__ == "__main__":
    main()



