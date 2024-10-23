import pytest

@pytest.fixture(scope="function")
def setup_function_scope():
    print("\n Setup: function scope fixture")

    yield
    print("Teardown:Fuction scope fixture")

def test_scope_1(setup_function_scope):
    print("Running test 1")
    assert True

def test_scope_2(setup_function_scope):
    print("Running test 2")
    assert True

