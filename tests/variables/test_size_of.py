import pytest

from tasks.variables.size_of import size_in_kb


@pytest.mark.parametrize(
    "some_object, expected", [
        ([i for i in range(100)], 0.9),
        ({i: i for i in range(100)}, 4.59),
    ]
)
def test_size_of(some_object, expected):
    assert size_in_kb(some_object) == expected
