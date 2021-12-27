import unittest
from tests.home.login_test import LoginTests
from tests.courses.register_course_csv_data import RegisterCourseCSVDataTests

#get all tests from the test classes

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(RegisterCourseCSVDataTests)


#create test suite

smokeTest = unittest.TestSuite([tc1,tc2])

unittest.TextTestRunner(verbosity=2).run(smokeTest)