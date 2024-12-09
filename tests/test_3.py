import pytest
from day3.solution import solve_part1, solve_part2, find_mul_operations, find_mul_operations_adv

input = "day3/test_input.txt"

@pytest.mark.parametrize(
    "line, expected_operations",
    [
        ("mul(2,4) and some text", [(2, 4)]),
        ("mul(3,7)mul(8,5)", [(3, 7), (8, 5)]),
        ("text without mul operations", []),
        ("mul(44,46) and mul(123,4)", [(44, 46), (123, 4)]),
        ("invalid mul(4*, mul(6,9!, ?(12,34), mul ( 2 , 4 )", []),
        ("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))", [(2, 4), (5,5), (11, 8), (8, 5)]),
    ],
)
def test_find_mul_operations_part1(line, expected_operations):
    assert find_mul_operations(line) == expected_operations


@pytest.mark.parametrize(
    "line, expected_operations",
    [
        ("xmul(2,4)%&mul[3,7]!@^don't()_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))", [(2, 4)]),
        ("xmul(2,4)%&mul[3,7]!@^don't()_mul(5,5)+mul(32,64]thendo()(mul(11,8)mul(8,5))", [(2, 4), (11, 8), (8, 5)]),

    ],
)
def test_find_mul_operations_part2(line, expected_operations):
    assert find_mul_operations_adv(line) == expected_operations


@pytest.mark.parametrize(
    "part, input_data, expected_output",
    [
        (1, input, 161),
        (2, input, 48),
    ],
)
def test_solve(part, input_data, expected_output):
    if part == 1:
        result = solve_part1(input_data)
    else:
        result = solve_part2(input_data)
    print(f"\n\n{result=}")
    assert result == expected_output