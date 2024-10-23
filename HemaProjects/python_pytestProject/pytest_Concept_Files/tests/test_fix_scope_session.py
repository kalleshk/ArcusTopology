#A fixture with scope="session" is executed once per test session (regardless of how many tests are run) and shared across all tests.

import  pytest

@pytest.fixture(scope="session")
def setup_session_scope():
    print("\nSetup:session scope fixture")
    resource = {"session_resource": "Initialized"}
    yield resource
    print("\n Teardown: Session scope fixture")

def test_session_scope_1(setup_session_scope):
    assert setup_session_scope["session_resource"] == "Initialized"


def test_session_scope_2(setup_session_scope):
    assert setup_session_scope["session_resource"] == "Initialized"
