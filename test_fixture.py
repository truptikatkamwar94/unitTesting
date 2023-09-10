import unittest
import pytest

@pytest.fixture
def setup():#method without test keyword called by test method using fixture
    print("\n setup method")
    
def test_fun1(setup):#1st approch
    print("Hekko")
    assert True

@pytest.mark.usefixtures("setup")#2nd approch
def test_fun2():
    print("dfjbgoidf")
    assert True

