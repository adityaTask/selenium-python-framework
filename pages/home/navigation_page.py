from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
from base.base import BasePage

class NavigationPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    _my_courses = "MY COURSES"
    _all_courses = "ALL COURSES"
    _home = "HOME"
    _user_icon = "//div[@class='dropdown']"

    def navigateToAllCourses(self):
        self.elementClick(self._all_courses,locatorType="link")

    def navigateToMyCourses(self):
        self.elementClick(self._my_courses, locatorType="link")

    def navigateToHome(self):
        self.elementClick(self._home, locatorType="link")

    def navigateToUserSettings(self):
        userSettingsElement =self.waitForElement(self._user_icon,locatorType="xpath",pollFrequency=5)
        self.elementClick(element=userSettingsElement)
