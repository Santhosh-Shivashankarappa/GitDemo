import pytest


@pytest.mark.usefixtures("provideData")
class SecondClass:

    @pytest.mark.smoke
    def test_firstProgram(self):
        msg = "hello"
        assert msg == "hello", "test failed"
        print("this is printed")

    @pytest.mark.sanity
    def test_secondProgram(self, provideData):
        msg = "hello"
        msg1 = "Hi"
        var = provideData
        print(var[1])
        assert msg == msg1, "test failed"
