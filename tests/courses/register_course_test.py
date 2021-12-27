from selenium import webdriver
from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TestStatus
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class RegisterCourseTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidEnroll(self):
        self.courses.enterCourseName("JavaScript")
        self.courses.selectCoursetoEnroll("JavaScript for beginners")
        self.courses.enrollCourse(num="1234 5678 9012 2092", exp="1224", cvv="444")
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result,
                          "Enrollment Failed Verification")