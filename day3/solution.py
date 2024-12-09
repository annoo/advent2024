import re

puzzle_input = "day3/input.txt"


def read_input(input_data) -> tuple[list[int], list[int]]:
    if isinstance(input_data, str) and '\n' in input_data:
        lines = input_data.strip().split('\n')
    else:
        with open(input_data, "r") as file:
            lines = file.read().strip().split('\n')
    return lines


def find_mul_operations(line):
    pattern = r'mul\((\d+),(\d+)\)'
    matches = re.findall(pattern, line)
    return [(int(x), int(y)) for x, y in matches]


def find_instructions(line):
    pattern = r'(do\(\)|don\'t\(\)|mul\(\d+,\d+\))'
    instructions = re.finditer(pattern, line)
    return [(match.group(), match.start()) for match in instructions]


def find_mul_operations_adv(line):
    instructions = find_instructions(line)
    mul_enabled = True
    valid_operations = []

    for instruction, _ in instructions:
        if instruction == 'do()':
            mul_enabled = True
        elif instruction == "don't()":
            mul_enabled = False
        elif mul_enabled and instruction.startswith('mul'):
            numbers = re.match(r'mul\((\d+),(\d+)\)', instruction)
            if numbers:
                x, y = map(int, numbers.groups())
                valid_operations.append((x, y))

    return valid_operations


def calculate_sum_of_products(operations):
    return sum(x * y for x, y in operations)


def solve_part1(input):
    lines = read_input(input)
    total = 0
    for line in lines:
        operations = find_mul_operations(line)
        total += calculate_sum_of_products(operations)
    return total
        


def solve_part2(input):
    lines = read_input(input)
    total = 0
    for line in lines:
        operations = find_mul_operations_adv(line)
        total += calculate_sum_of_products(operations)
    return total


if __name__ == "__main__":
    solution1 = solve_part1(puzzle_input)
    solution2 = solve_part2(puzzle_input)
    print(f"\n\nsolution part 1 : {solution1}")
    print(f"\nsolution part 2 : {solution2}")