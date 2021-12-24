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

def get_windows(data: list[int], window_size: int) -> list[list[int]]:
    return [data[i:i+window_size] for i in range(len(data)-window_size+1)]

def sum_windows(windows: list[list[int]]) -> list[int]:
    return [sum(win) for win in windows]

def count_increases(data: list[int]) -> int:
    return sum([1 for a,b in zip(data[:-1], data[1:]) if (b-a) > 0])

if __name__ == "__main__":
    filename = get_input_filename()
    measurements = read_measurments(filename)
    print(count_increases(sum_windows(get_windows(measurements, 3))))