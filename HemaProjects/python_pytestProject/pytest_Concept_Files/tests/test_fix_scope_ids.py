import pytest

@pytest.fixture(params=[1,2,3], ids=["apple","banana","cherry"])
def setup_with_ids(request):
    return request.param

def test_with_ids(setup_with_ids):
    assert setup_with_ids in [1, 2, 3]

 #output
# test_fix_scope_ids.py::test_with_ids[apple]
# test_fix_scope_ids.py::test_with_ids[banana]
# test_fix_scope_ids.py::test_with_ids[cherry]
