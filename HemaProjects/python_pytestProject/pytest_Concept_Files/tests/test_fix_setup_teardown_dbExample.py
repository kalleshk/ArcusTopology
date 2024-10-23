import pytest

#Define fixture
@pytest.fixture()

#define a setup and teardown

def setup_teardown():
    #setup code

    print("\nSetup: Open database connection")
    db = {"dbconnection":"open"}
    yield db

    #teardown Phase
    print("Teardown: Close database connection")
    db["dbconnection"] = 'closed'

#test db connection using  fixture
def test_dbconnection(setup_teardown):
    data = setup_teardown
    assert data['dbconnection'] == "open"




