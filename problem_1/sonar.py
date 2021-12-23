import argparse

def read_measurments(filename: str) -> list[int]:
    with open(filename) as input_file:
        measurementes = [int(line) for line in input_file]
    return measurementes

def count_increases(measurements: list[int], verbose: bool = False) -> int:
    if verbose:
        print("Haha, Adam was lazy and didn't impliment this. Sorry!")

    # NOTE: There has to be a more clever way to do this but oh well for now
    num_increases = 0
    for i in range(1,len(measurements)):
        if measurments[i] > measurments[i-1]:
            num_increases += 1
    return num_increases

def get_input_filename() -> str:
    # NOTE: Argparse is probably overkill for one positional argument but oh well
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', nargs='?', default='./input.txt')

    args = parser.parse_args()
    filename = args.input_file
    return filename

if __name__ == "__main__":
    filename = get_input_filename()
    measurments = read_measurments(filename)
    print(count_increases(measurments))