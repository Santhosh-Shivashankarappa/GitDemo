import pytest


@pytest.fixture(scope="class")
def setup():
    print("setting up the browser")
    yield
    print("closing the browser")


@pytest.fixture()
def provideData():
    print("User profile data is being created")
    return ["santhosh", "chaitra", "devansh"]
