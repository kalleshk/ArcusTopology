
import pytest

@pytest.fixture(scope="class")
def setup_class_scope():
    print("\n Setup:class scope fixture")
    resource = {"class_resource": "Initialized"}

    yield resource
    print("\n Teardown: Class scope fixture")

class TestExample:
    def test_class_scope_1(self, setup_class_scope):
        assert setup_class_scope["class_resource"] == "Initialized"

    def test_class_scope_2(self, setup_class_scope):
        assert setup_class_scope["class_resource"] == "Initialized"
