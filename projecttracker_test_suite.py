import unittest
from TestFile_Handler import TestFile_Handler
from TestInput_Handler import TestInput_Handler
from TestOperations import TestOperations

def my_suite():
    test_suite = unittest.TestSuite()
    result = unittest.TestResult()
    test_suite.addTest(unittest.makeSuite(TestFile_Handler))
    test_suite.addTest(unittest.makeSuite(TestInput_Handler))
    test_suite.addTest(unittest.makeSuite(TestOperations))
    runner = unittest.TextTestRunner()
    print(runner.run(test_suite))
    return test_suite

my_suite()