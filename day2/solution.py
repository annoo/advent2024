from typing import Iterator

puzzle_input = "day2/input.txt"


def read_input(input_data) -> list[list[int]]:
    if isinstance(input_data, str) and '\n' in input_data:
        lines = input_data.strip().split('\n')
    else:
        with open(input_data, "r") as file:
            lines = file.readlines()
    
    reports = []

    for line in lines:
        report = list(map(int, line.strip().split()))
        reports.append(report)

    return reports

def is_increasing_slowly(report: list[int]) -> bool:
    for i in range(len(report) - 1):
        current_level = report[i]
        next_level = report[i + 1]

        difference = next_level - current_level
        if difference < 1:
            return False
        if difference > 3:
            return False
    return True
            

def is_decreasing_slowly(report: list[int]) -> bool:
    for i in range(len(report) - 1):
        current_level = report[i]
        next_level = report[i + 1]

        difference = current_level - next_level
        if difference < 1:
            return False
        if difference > 3:
            return False
    return True

def solve_part1(input):
    reports = read_input(input)
    number_of_safe_reports = 0
    for report in reports:
        if is_increasing_slowly(report):
            number_of_safe_reports += 1
        elif is_decreasing_slowly(report):
            number_of_safe_reports += 1
    return number_of_safe_reports


def create_modified_report(report: list[int]) -> Iterator[list[int]]:
    for i in range(len(report)):
        yield report[:i] + report[i + 1:]


def solve_part2(input):
    reports = read_input(input)
    number_of_safe_reports = 0
    for report in reports:
        if is_increasing_slowly(report) or is_decreasing_slowly(report):
            number_of_safe_reports += 1
        else:
          for modified_report in create_modified_report(report):
              if is_increasing_slowly(modified_report) or is_decreasing_slowly(modified_report):
                  number_of_safe_reports += 1
                  break
    return number_of_safe_reports


def generate_solution(puzzle):
    solution1 = solve_part1(puzzle)
    solution2 = solve_part2(puzzle)
    print(f"\n\nsolution part 1 : {solution1}")
    print(f"\nsolution part 2 : {solution2}")


if __name__ == "__main__":
    solution1 = solve_part1(puzzle_input)
    solution2 = solve_part2(puzzle_input)
    print(f"\n\nsolution part 1 : {solution1}")
    print(f"\nsolution part 2 : {solution2}")

