import csv
from itertools import izip


def chart():
    with open('out_Students_2012.txt', 'rb') as score_csv, open('out_Students_When.txt') as when_csv:
