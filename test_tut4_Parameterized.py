from tut4 import add
import pytest
def test_add_num():
    assert add(3,3)

def test_add_str():
    assert add("a","b")=="ab"

def test_add_list():
    assert add([1,2],[3])==[1,2,3]



@pytest.mark.parametrize("a,b,c",[(1,2,3),("a","b","ab"),([1,2],[3],[1,2,3])])
def test_add(a,b,c):
    assert add(a,b)==c

#OR
#if you want to give id's to test to identify
@pytest.mark.parametrize("a,b,c",[(1,2,3),("a","b","ab"),([1,2],[3],[1,2,3])],ids=["num","str","list"])
def test_add(a,b,c):
    assert add(a,b)==c