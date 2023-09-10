import pytest
@pytest.fixture(autouse=True)
def setup():
    print("\n setup")
def test_fun1():
    print("Hello")
    assert True


def test_fun2():
    print("world")
    assert True


