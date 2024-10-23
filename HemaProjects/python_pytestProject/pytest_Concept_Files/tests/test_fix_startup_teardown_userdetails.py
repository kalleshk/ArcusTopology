import pytest

#Define fixture

@pytest.fixture
#define setupcode
def setup_teardown():
    #setup code
    print("\n Setup the user creditional")
    user_details = {"username":"Jhonson", "password":"Jhonson123", "email":"Jhonson@gmail.com"}
    yield user_details

    #Teardown phase
    print("\n Clearing or rest the  user data")


#test user details
def test_Userdetails(setup_teardown):
    user_data = setup_teardown
    assert user_data["username"] == "Jhonson"
    assert user_data["email"] == "Jhonson@gmail.com"
    assert user_data["password"] == "Jhonson123"








