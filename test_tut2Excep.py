from tut2 import validate_age
import pytest 
class Testvalidate:
    def test_validate_age(self):
        validate_age(10)

    def test_validate_age_invalid_age_1(self):
        with pytest.raises(ValueError) as excep_info:
            validate_age(9)
        print(str(excep_info.value))
        assert str(excep_info.value)=="Age cannot be less than zero"


    #or prepf
    def test_validate_age_invalid_age_2(self):
        with pytest.raises(ValueError,match="Age cannot be less than zero"):
            validate_age(-3)
