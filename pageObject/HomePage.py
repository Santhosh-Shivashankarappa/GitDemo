from selenium.webdriver.common.by import By

from pageObject.CheckoutPage import CheckoutPage


class HomePage:
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkBox = (By.ID, "exampleCheck1")
    genderDropDown = (By.ID, "exampleFormControlSelect1")
    submitBtn = (By.XPATH, "//input[@value='Submit']")
    successMsg = (By.CSS_SELECTOR, "[class*='alert-success']")
    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    def __init__(self, driver):
        self.driver = driver

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def clickCheckBox(self):
        return self.driver.find_element(*HomePage.checkBox)

    def getGenderDropDown(self):
        return self.driver.find_element(*HomePage.genderDropDown)

    def getSubmitBtn(self):
        return self.driver.find_element(*HomePage.submitBtn)

    def getSuccessMsg(self):
        return self.driver.find_element(*HomePage.successMsg)

    def shopItem(self):
        self.driver.find_element(*HomePage.shop).click()
        return CheckoutPage(self.driver)
