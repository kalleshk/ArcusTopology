import pytest

@pytest.fixture(scope="module")

def setup_scope_module():
    print("\nSetup: Preparing for fixture module scope")

    resource = {"module_resource": "Active"}
    yield resource

    #teardown phase
    print("Teardown: Module scope fixture")

def test_module_scope1(setup_scope_module) :
    assert setup_scope_module["module_resource"] == "Active"

def test_module_scope2(setup_scope_module) :
    assert setup_scope_module["module_resource"] == "Active"





