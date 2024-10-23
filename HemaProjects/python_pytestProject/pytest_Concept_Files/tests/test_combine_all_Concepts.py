import pytest

@pytest.fixture(scope="session",autouse=True)
def setup_session():
    print("\nSetup: Session-wide resource")
    yield
    print("Teardown: Session-wide Resource")

@pytest.fixture(scope="class")
def setup_class():
    print("\nSetup: class-wide resource")
    yield
    print("Teardown: Class-wide Resource")

@pytest.fixture(params=[10,20],ids=["ten", "twenty"])
def setup_parameterized(request):
    print(f"\nSetup: Parameterized fixture with {request.param}")
    yield request.param
    print(f"Teardown: Parameterized fixture with {request.param}")

class TestSuite:
    def test_case_1(self,setup_class,setup_parameterized):
        print("Test Case 1")
        assert setup_parameterized in [10, 20]

    def test_case_2(self,setup_class,setup_parameterized):
        print("Test Case 2")
        assert setup_parameterized * 2 in [20, 40]



