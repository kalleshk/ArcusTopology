import pytest
import  os

@pytest.fixture

def create_temp_file(tmpdir):
    #setup create a temporary file
    temp_file=tmpdir.join("tempfile.txt")
    temp_file.write("Hello, World!")
    yield temp_file
    # No explicit teardown needed; pytest will remove the temp directory

def test_temp_file(create_temp_file):
    # Verify the file was created and has content
    assert os.path.exists(str(create_temp_file))
    assert create_temp_file.read() == "Hello, World!"

