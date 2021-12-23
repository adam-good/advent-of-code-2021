
def read_measurments(filename: str) -> list[int]:
    with open(filename) as input_file:
        measurementes = [int(line) for line in input_file]
    return measurementes

def count_increases(measurements: list[int], verbose: bool = False) -> int:
    # NOTE: There has to be a more clever way to do this but oh well for now
    num_increases = 0
    for i in range(1,len(measurements)):
        if measurments[i] > measurments[i-1]:
            num_increases += 1
    return num_increases

if __name__ == "__main__":
    measurments = read_measurments("test_input.txt")
    print(count_increases(measurments))