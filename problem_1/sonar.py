import argparse
import numpy as np
import matplotlib.pyplot as plt
import time
import multiprocess
import math

def get_input_filename() -> str:
    # NOTE: Argparse is probably overkill for one positional argument but oh well
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', nargs='?', default='./input.txt')

    args = parser.parse_args()
    filename = args.input_file
    return filename

def read_measurments(filename: str) -> list[int]:
    with open(filename) as input_file:
        measurementes = [int(line) for line in input_file]
    return measurementes

def count_increases(measurements: list[int]) -> int:
    return sum([1 for a,b in zip(measurements[:-1], measurements[1:]) if (b-a) > 0])

if __name__ == "__main__":
    filename = get_input_filename()
    measurements = read_measurments(filename)
    print(count_increases(measurements))