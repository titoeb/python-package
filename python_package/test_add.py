import pytest

add_test_grid = [
    # a, b, expected_result
    (1, 1, 2),
    (2, 2, 4),
    (100, 1, 101)
]

@pytest.mark.parametrize('a,b,expected_result', add_test_grid)
def test_add(a: int, b: int, expected_result: int):
    assert a + b == expected_result
