import pytest
@pytest.fixture
def setup1():
    print("\n setup1")
    yield
    print("\n Teardown")


@pytest.fixture()
def setup2(request):
    print("\n setup2")

    def teardown_a():
        print("\n Teardown A")

    def teardown_b():
        print("\n Teardown B")


    request.addfinalizer(teardown_a)
    request.addfinalizer(teardown_b)

def test1(setup1):
    print("Execution test1")


def test2(setup2):
    print("Execution test2")