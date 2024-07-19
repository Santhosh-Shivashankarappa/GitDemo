from selenium.webdriver.common.by import By

from pageObject.ConfirmPage import ConfirmationPage


class CheckoutPage:
    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    addItem = (By.CSS_SELECTOR, ".card-footer button")
    checkoutBtn = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def __init__(self, driver):
        self.driver = driver

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getAddItemsBtn(self):
        return self.driver.find_elements(*CheckoutPage.addItem)

    def getCheckoutBtn(self):
        self.driver.find_element(*CheckoutPage.checkoutBtn).click()
        return ConfirmationPage(self.driver)
