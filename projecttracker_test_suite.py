import unittest
from testfile import TestFile_Handler
from testinput import TestInput_Handler
from testop import TestOperations

def projecttracker_test_suite():
    test_suite = unittest.TestSuite()
    result = unittest.TestResult()
    test_suite.addTest(unittest.makeSuite(TestFile_Handler))
    test_suite.addTest(unittest.makeSuite(TestInput_Handler))
    test_suite.addTest(unittest.makeSuite(TestOperations))
    runner = unittest.TextTestRunner()
    return test_suite