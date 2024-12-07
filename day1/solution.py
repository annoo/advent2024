puzzle_input = "day1/input.txt"


def read_input(input_data) -> list[list[int]]:
    location_ID1 = []
    location_ID2 = []
    
    if isinstance(input_data, str) and '\n' in input_data:
        lines = input_data.strip().split('\n')
    else:
        with open(input_data, "r") as file:
            lines = file.readlines()

    for line in lines:
        left, right = map(int, line.strip().split())
        
        location_ID1.append(left)
        location_ID2.append(right)

        location_ID2.sort()
        location_ID1.sort()

    return [location_ID1, location_ID2]


def calculate_total_difference(location1: list[int], location2: list[int]) -> int:  
    differences = map(lambda x, y: abs(x - y), location1, location2)
    total_difference = sum(differences)
    return total_difference


def solve_part1(input):
    locationID1, locationID2 = read_input(input)
    total_difference = calculate_total_difference(locationID1, locationID2)
    return total_difference


if __name__ == "__main__":
    solution1 = solve_part1(puzzle_input)
    # solution2 = solve_part2(puzzle)
    print(f"\n\nsolution part 1 : {solution1}")
    # print(f"\nsolution part 2 : {solution2}")