import pytest
#Define a  Fixture
@pytest.fixture
def setup_and_tear_down():
    #set Up code
    print("\nSetup: Preparing resources...")
    test_data = {"name":"Ram", "age":50}
    #Yielding allows the test to run here

    yield test_data

    # Teardown code

    print("\nTeardown: Cleaning up resources...")

# Test function using the fixture
def test_example(setup_and_tear_down):
    # Access the fixture data
    data = setup_and_tear_down
    assert data['name'] =='Ram'
    assert data['age'] == 50



