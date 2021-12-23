import argparse

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