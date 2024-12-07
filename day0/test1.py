import pytest
from day1.solution import solve_part1, solve_part2


@pytest.mark.parametrize(
    "part, input_data, expected_output",
    [
        (1, "input_1", 1),
        #(2, "input_1", 281),
    ],
)
def test_solve(part, input_data, expected_output):
    if part == 1:
        result = solve_part1(input_data)
    else:
        result = solve_part2(input_data)
    print(f"\n\n{result=}")
    assert result == expected_output