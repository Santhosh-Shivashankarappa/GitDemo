from selenium.webdriver.common.by import By


class ConfirmationPage:
    checkoutConfirmBtn = (By.XPATH, "//button[@class='btn btn-success']")
    enterCountryName = (By.ID, "country")
    countryName = (By.LINK_TEXT, "India")
    checkBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchaseBtn = (By.CSS_SELECTOR, "[type='submit']")
    successMsg = (By.CSS_SELECTOR, "[class*='alert alert-success']")

    def __init__(self, driver):
        self.driver = driver

    def getCheckoutConfirmBtn(self):
        return self.driver.find_element(*ConfirmationPage.checkoutConfirmBtn)

    def getCountryName(self):
        return self.driver.find_element(*ConfirmationPage.enterCountryName)

    def isCountryNamePresent(self):
        return self.driver.find_element(*ConfirmationPage.countryName)

    def clickCheckBox(self):
        return self.driver.find_element(*ConfirmationPage.checkBox)

    def clickPurchaseBtn(self):
        return self.driver.find_element(*ConfirmationPage.purchaseBtn)

    def getSuccessMsg(self):
        return self.driver.find_element(*ConfirmationPage.successMsg)
