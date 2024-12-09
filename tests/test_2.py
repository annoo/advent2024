import pytest
from day2.solution import solve_part1, solve_part2, create_modified_report

input = "day2/test_input.txt"

@pytest.mark.parametrize(
    "report, expected_outputs",
    [
        ([7, 6, 4, 2, 1], [[6, 4, 2, 1], [7, 4, 2, 1], [7, 6, 2, 1], [7, 6, 4, 1], [7, 6, 4, 2]]),
        ([1, 2, 7, 8, 9], [[2, 7, 8, 9], [1, 7, 8, 9], [1, 2, 8, 9], [1, 2, 7, 9], [1, 2, 7, 8]]),
        ([9, 7, 6, 2, 1], [[7, 6, 2, 1], [9, 6, 2, 1], [9, 7, 2, 1], [9, 7, 6, 1], [9, 7, 6, 2]]),
        ([1, 3, 2, 4, 5], [[3, 2, 4, 5], [1, 2, 4, 5], [1, 3, 4, 5], [1, 3, 2, 5], [1, 3, 2, 4]]),
        ([8, 6, 4, 4, 1], [[6, 4, 4, 1], [8, 4, 4, 1], [8, 6, 4, 1], [8, 6, 4, 1], [8, 6, 4, 4]]),
        ([1, 3, 6, 7, 9], [[3, 6, 7, 9], [1, 6, 7, 9], [1, 3, 7, 9], [1, 3, 6, 9], [1, 3, 6, 7]]),
    ],
)
def test_create_modified_report(report, expected_outputs):
    result = list(create_modified_report(report))
    assert result == expected_outputs


@pytest.mark.parametrize(
    "part, input_data, expected_output",
    [
        (1, input, 2),
        (2, input, 4),
    ],
)
def test_solve(part, input_data, expected_output):
    if part == 1:
        result = solve_part1(input_data)
    else:
        result = solve_part2(input_data)
    print(f"\n\n{result=}")
    assert result == expected_output