from tut1 import function


class TestFunction:
    def test_function(self):
        assert function(3,6)==9

    def test_add_str(self):
        assert function("nksd","bkjd")=="nksdbkjd"