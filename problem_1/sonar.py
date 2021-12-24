import argparse
import numpy as np
import matplotlib.pyplot as plt
import time
import multiprocess
import math

def read_measurments(filename: str) -> list[int]:
    with open(filename) as input_file:
        measurementes = [int(line) for line in input_file]
    return measurementes

def count_increases_imparative(measurements: list[int]) -> int:
    num_increases = 0
    for i in range(1,len(measurements)):
        if measurements[i] > measurements[i-1]:
            num_increases += 1
    return num_increases

def count_increases_functional(measurements: list[int]) -> int:
    return sum([1 for a,b in zip(measurements[:-1], measurements[1:]) if (b-a) > 0])

def _time_function(fn, verbose=False) -> float:
    start_time = time.time()
    fn()
    end_time = time.time()

    if verbose: print(f"Function took {end_time - start_time} to complete")

    return end_time 

def _compare_functions():
    points_imp = []
    points_fnc = []
    scales = [2**a for a in range(26)]

    def sample_fn_serial(fn, scale, n_samples):
        return np.mean([
            _time_function(lambda: fn(np.random.randint(0,1000,scale)))
            for _ in range(n_samples)
        ])

    # Look, my macbook was taking a bit. This helped. Don't judge
    def sample_fn_parallel(fn,scale,n_samples):
        with multiprocess.Pool(16) as pool:
            return np.mean(pool.map(_time_function, [lambda: fn(np.random.randint(0,1000,scale)) for _ in range(n_samples)]))

    sample_fn = sample_fn_parallel

    for s in scales:
        print(f"{math.log(s,2)}", end='\r')
        t1 = time.time()
        sample_imp = sample_fn(count_increases_imparative, s, 16)
        sample_fnc = sample_fn(count_increases_functional, s, 16)
        t_diff = time.time() - t1
        points_imp.append(sample_imp)
        points_fnc.append(sample_fnc)
        print(f"{math.log(s,2)} {t_diff}", end='\r')
        print()

    plt.plot(scales, points_imp, marker='o', linestyle='-', label="imparitive")
    plt.plot(scales, points_fnc, marker='o', linestyle='-', label="functional")
    plt.xscale('log', base=2)
    plt.legend()
    plt.savefig('./output/scaling_study.png')
    plt.show()

def get_input_filename() -> str:
    # NOTE: Argparse is probably overkill for one positional argument but oh well
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', nargs='?', default='./input.txt')

    args = parser.parse_args()
    filename = args.input_file
    return filename

if __name__ == "__main__":
    filename = get_input_filename()
    measurements = read_measurments(filename)
    print(count_increases_imparative(measurements))
    print(count_increases_functional(measurements))