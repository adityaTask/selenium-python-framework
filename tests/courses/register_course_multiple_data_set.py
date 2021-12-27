from selenium import webdriver
from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TestStatus
import unittest
import pytest
from ddt import ddt,data,unpack


@pytest.mark.usefixtures("oneTimeSetUp","setUp")
@ddt
class RegisterCourseTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(("JavaScript for beginners","10","1224","124"),
          ("Learn Python 3 from scratch","10","1224","124"))
    @unpack
    def test_invalidEnroll(self,courseName,ccNum,ccExp,ccCVV):
        self.courses.enterCourseName(courseName)
        self.courses.selectCoursetoEnroll(courseName)
        self.courses.enrollCourse(num=ccNum, exp=ccExp, cvv=ccCVV)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result,
                          "Enrollment Failed Verification")