import utilities.custom_logger as cl
import logging
from base.base import BasePage
from pages.home.navigation_page import NavigationPage

class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(self.driver)

    #locators
    _login_link = "//a[@href='/login']"
    _email_field = "email"
    _password_field = "password"
    _login_button = "//input[@value='Login']"

    def clickLoginLink(self):
        self.elementClick(self._login_link,locatorType="xpath")

    def enterUserName(self,email):
        self.sendKeys(email,self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password,self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button,locatorType="xpath")

    def login(self,email="",password=""):
        self.clickLoginLink()
        self.enterUserName(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccess(self):
        result = self.isElementPresent("dropdownMenu1")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//span[contains(text(),'Your username or password is invalid. Please try again.')]",
                                       locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("My Courses")

    def logout(self):
        self.nav.navigateToUserSettings()
        logoutLinkELement = self.waitForElement(locator="//a[@href='/logout']",locatorType="xpath",pollFrequency=5)
        self.elementClick(element=logoutLinkELement)










