from datetime import datetime
import pytest
from tut7 import Student,get_topper

@pytest.fixture
def dummy_student():
    return Student("company",datetime(2022,10,10),"coe",90)

@pytest.fixture
def make_student_factory():
    def _make_dummy_student(name,credits):
        return Student(name,datetime(2022,10,10),"coe",credits)
    return _make_dummy_student

def test_student_get_age(dummy_student):
    dummy_student_age=(datetime.now()-dummy_student.dob).days//365
    assert dummy_student.get_age()==dummy_student_age

def test_student_get_credits(dummy_student):
    assert dummy_student.get_credits()==90

def test_get_topper(make_student_factory):
    students=[
       make_student_factory("ram",21),
        make_student_factory("dfjksd",54),
        make_student_factory("sglsd",1000)
    ]
    topper=get_topper(students)
    print("Topperr=>",topper)
    assert topper==students[2]