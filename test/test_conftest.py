import conftest

def test_conftest():
    assert conftest.option.Database
    assert conftest.option.Database == "mysql://localhost/test?fest=pest"
