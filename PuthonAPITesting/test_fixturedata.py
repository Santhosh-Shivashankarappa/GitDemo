import pytest


@pytest.mark.usefixtures("provideData")
class FetchData:

    def editProfile_test(self, provideData):
        print(provideData)

    def editProfile_test1(self, provideData):
        print(provideData[0])
        print(provideData[1])
        print(provideData[2])
