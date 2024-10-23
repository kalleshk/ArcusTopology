import pytest

@pytest.fixture(autouse=True)
def setup_autouse():
    print("\nSetup: Autouse fixture")
    yield
    print("\nTeardown: Autouse fixture")

def test_autouse_1():
    print("Running test 1")
    assert True

def test_autouse_2():
    print("Running test 2")
    assert True
