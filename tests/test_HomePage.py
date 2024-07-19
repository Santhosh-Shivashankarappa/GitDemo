import time

import pytest
from selenium.webdriver.support.select import Select

from TestData.HomePageTestData import HomePageTestData
from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        homePage = HomePage(self.driver)
        homePage.getName().send_keys(getData["FirstName"])
        homePage.getEmail().send_keys(getData["Email"])
        homePage.getPassword().send_keys("Test@123")
        # dropDown = Select(homePage.getGenderDropDown())
        # dropDown.select_by_index(1)
        self.selectOptionByText(homePage.getGenderDropDown(), getData["Gender"])
        homePage.getSubmitBtn().click()
        alertText = homePage.getSuccessMsg().text

        assert ("Success!" in alertText)
        self.driver.refresh()

    @pytest.fixture(params=HomePageTestData.test_HomePageData)
    def getData(self, request):
        return request.param
