import time

from base.base import BasePage
from utilities import custom_logger as cl
import logging
from pages.home.navigation_page import NavigationPage

class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(self.driver)
    #locators

    _all_courses = "//*[@id='navbar-inverse-collapse']//a[@href = '/courses'][position()=1]"
    _search_course ="//input[@id='search']"
    _search_button = "//*[@id='search']//button"
    _course = "//h4[contains(text(),'{0}')]"
    _enroll_course = "//*[contains(text(),'Enroll in Course')]"
    _cc_num = "//input[@name = 'cardnumber']"
    _frame_cc_num ="//iframe[@title='Secure card number input frame']"
    _cc_exp = "//input[@name = 'exp-date']"
    _frame_cc_exp ="//iframe[@title='Secure expiration date input frame']"
    _cc_cvv = "//input[@name = 'cvc']"
    _frame_cc_cvv = "//iframe[@title='Secure CVC input frame']"
    _buy = "//*[@id='checkout-form']/div[2]/div[3]/div/div[1]/div[2]/div/button[1]"
    _enroll_error_message = "//span[text()='Your card number is incomplete.']"



    def enterCourseName(self, name):
        self.nav.navigateToAllCourses()
        #self.elementClick(self._all_courses, 'xpath')
        self.sendKeys(name, locator=self._search_course,locatorType="xpath")
        self.elementClick(locator=self._search_button,locatorType="xpath")

    def selectCoursetoEnroll(self,fullCourseName):
        self.elementClick(self._course.format(fullCourseName),'xpath')

    def clickOnEnrollButton(self):
        self.elementClick(self._enroll_course,'xpath')

    def enterCardNum(self,num):
        self.driver.switch_to.frame(self.getElement(self._frame_cc_num, "xpath"))
        self.sendKeys(num, self._cc_num, 'xpath')
        self.driver.switch_to.default_content()

    def enterCardExp(self,exp):
        self.driver.switch_to.frame(self.getElement(self._frame_cc_exp, "xpath"))
        self.sendKeys(exp, self._cc_exp, 'xpath')
        self.driver.switch_to.default_content()

    def enterCardCVV(self,cvv):
        self.driver.switch_to.frame(self.getElement(self._frame_cc_cvv, "xpath"))
        self.sendKeys(cvv, self._cc_cvv, 'xpath')
        self.driver.switch_to.default_content()

    def clickBuy(self):
        self.elementClick(self._buy,'xpath')

    def enterCCInformation(self,num,exp,cvv):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)

    def enrollCourse(self,num,exp,cvv):
        self.clickOnEnrollButton()
        self.webScroll("down")
        self.enterCCInformation(num,exp,cvv)
        self.clickBuy()

    def verifyEnrollFailed(self):
        result = self.isElementDisplayed(self._enroll_error_message,"xpath")
        return result


