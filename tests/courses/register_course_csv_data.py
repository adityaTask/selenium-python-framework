from selenium import webdriver
from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TestStatus
import unittest
import pytest
from ddt import ddt,data,unpack
from utilities.read_data import getCSVData


@pytest.mark.usefixtures("oneTimeSetUp","setUp")
@ddt
class RegisterCourseCSVDataTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(*getCSVData("D:\\workspace_python\\LetsKodeit\\testdata.csv"))
    #@data([['JavaScript for beginners', '10', '1220', '10'], ['Learn Python 3 from scratch', '20', '1220', '20']])
    @unpack
    def test_invalidEnroll(self,courseName,ccNum,ccExp,ccCVV):
        self.courses.enterCourseName(courseName)
        self.courses.selectCoursetoEnroll(courseName)
        self.courses.enrollCourse(num=ccNum, exp=ccExp, cvv=ccCVV)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result,
                          "Enrollment Failed Verification")