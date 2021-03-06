import time

from selenium import webdriver
from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)


    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("task.aditya.95@gmail.com","killedarrox")
        result1 = self.lp.verifyLoginTitle()
        self.ts.mark(result1,"Title is incorrect")
        result2 = self.lp.verifyLoginSuccess()
        self.ts.markFinal("test_validLogin",result2,"Login was successful")

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.logout()
        self.lp.login("test@gmail.com","test")
        time.sleep(2)
        result = self.lp.verifyLoginFailed()
        assert result == True