from tut3 import function
import pytest
import sys
@pytest.mark.skip(reason="I dont want this test")
def test_function1():
    assert function(3,5)==8


@pytest.mark.skipif(10>3,reason="10 is grater than 3")
def test_function2():
    assert function("a","b")=="ab"


#you know your code can throw exception,but are okk with that
@pytest.mark.Xfail(13>5)
def test_function_list():
    assert function([1],[4])==[1,4]
    raise Exception()
