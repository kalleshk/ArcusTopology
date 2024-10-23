import pytest

@pytest.fixture(name="custom_fixture_name")

def setup_custom_name():
    print("\nSetup: Custom named fixture")
    return {"key" : "value"}

def test_custom_name(custom_fixture_name):
    assert custom_fixture_name["key"] == "value"


