import pytest


def test_program_one():
    msg = "Hello"
    assert msg == "HELLO", "both the strings doesnot match"

@pytest.mark.smoke
def test_math():
    a = 2
    b = 4
    assert a + 2 == b, "values doesnot match"
