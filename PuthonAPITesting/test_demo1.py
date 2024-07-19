import pytest


@pytest.mark.usefixtures("setup")
class Test1_Examples:

    def test_firstProgram(self):
        print("hello")

    @pytest.mark.smoke
    def test_secondProgram(self):
        print("Hi")

    def test_thirdProgram(self):
        print("Hi")

    def test_fourthProgram(self):
        print("Hi")
