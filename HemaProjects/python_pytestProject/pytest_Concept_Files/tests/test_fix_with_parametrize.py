import pytest

@pytest.fixture
def get_user_data():
    return {"name": "Alice", "age": 28}

@pytest.mark.parametrize("age, expected_result",[(28, True),(40, False)])

def test_user_data(get_user_data, age, expected_result):
    userdata = get_user_data
    assert (userdata['age'] == age) == expected_result
