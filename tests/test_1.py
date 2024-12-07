import pytest
from day1.solution import solve_part1, solve_part2

input = "day1/test_intput.txt"

@pytest.mark.parametrize(
    "part, input_data, expected_output",
    [
        (1, input, 11),
        (2, input, 31),
    ],
)
def test_solve(part, input_data, expected_output):
    if part == 1:
        result = solve_part1(input_data)
    else:
        result = solve_part2(input_data)
    print(f"\n\n{result=}")
    assert result == expected_output