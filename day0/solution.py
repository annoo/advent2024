puzzle_input = "input.txt"


def read_input(input_file) -> tuple[list[int], list[int]]:
    with open(input_file, "r") as file:
        for line in file:
            pass
        return 1

def solve_part1(input_data):
    return 1

def generate_solution(puzzle):
    solution1 = solve_part1(puzzle)
    solution2 = solve_part2(puzzle)
    print(f"\n\nsolution part 1 : {solution1}")
    print(f"\nsolution part 2 : {solution2}")

if __name__ == "__main__":
    _input = puzzle_input
    generate_solution(_input)