import time

from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutPage = homePage.shopItem()
        log.info("Getting all the card titles ")
        cardTitles = checkoutPage.getCardTitles()
        i = -1
        for cardTitle in cardTitles:
            i = i + 1
            cardTitleText = cardTitle.text
            log.info(cardTitleText)
            if cardTitleText == "Blackberry":
                checkoutPage.getAddItemsBtn()[i].click()

        confirmationPage = checkoutPage.getCheckoutBtn()

        confirmationPage.getCheckoutConfirmBtn().click()
        confirmationPage.getCountryName().send_keys("ind")
        self.verifyLinkTextPresence("India")

        confirmationPage.isCountryNamePresent().click()
        confirmationPage.clickCheckBox().click()
        confirmationPage.clickPurchaseBtn().click()
        textMatch = confirmationPage.getSuccessMsg().text

        assert ("Success! Thank you!" in textMatch)

        time.sleep(3)
