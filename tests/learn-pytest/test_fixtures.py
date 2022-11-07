import pytest

@pytest.fixture
def input_value():
    return 20

# tests

def test_divisible_by_3(input_value):
    assert input_value % 3 != 0

def test_divisible_by_2(input_value):
    assert input_value % 2 == 0



