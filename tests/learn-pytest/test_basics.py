import pytest
#make sure to start function name with test
def test_sum():
    assert sum([1, 2], 3) == 6

def test_assert_type():
    assert type(sum([1,2], 3)) is int



