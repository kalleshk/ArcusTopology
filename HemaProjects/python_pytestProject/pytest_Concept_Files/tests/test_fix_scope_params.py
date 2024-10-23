import  pytest

@pytest.fixture(params=[1,2,3])
def setup_scope_params(request):
    param = request.param

    print(f"\nSetup: Param {param}")
    return param

def test_params(setup_scope_params):
    assert setup_scope_params in [1, 2, 3]
