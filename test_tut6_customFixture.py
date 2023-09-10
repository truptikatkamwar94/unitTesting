from tut6 import Student
from datetime import datetime
import pytest

@pytest.fixture(scope="module")#instead of creating obj at every time in each test function , use fixture[scope define  dummy_student is valid for function/class/module]
def dummy_student():
    print("object creation using fixture**")
    return Student('Posit',datetime(2000,1,1),"coe")

def test_student_get_age(dummy_student):
    dummy_student_age=(datetime.now()-dummy_student.dob).days//365
    assert dummy_student.get_age()==dummy_student_age



def test_student_add_credits(dummy_student):
    dummy_student.add_credits(5)
    assert dummy_student.get_credits()==5


def test_studdent_get_credits(dummy_student):
    dummy_student.get_credits()==0