'''
Created on Oct 9, 2012

@author: timo
'''
from duration import duration
from datetime import timedelta
import unittest

class DurationTestCase(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(duration(timedelta(seconds = 1), "%s"), "01")
        self.assertEqual(duration(timedelta(seconds = 60), "%s"), "00")
        self.assertEqual(duration(timedelta(seconds = 1), "%S"), "01")
        self.assertEqual(duration(timedelta(seconds = 60), "%S"), "60")
        self.assertEqual(duration(timedelta(minutes = 1), "%S"), "60")
        self.assertEqual(duration(timedelta(minutes = 2), "%S"), "120")
        self.assertEqual(duration(timedelta(minutes = 1), "%m"), "01")
        self.assertEqual(duration(timedelta(minutes = 60), "%m"), "00")
        self.assertEqual(duration(timedelta(minutes = 1), "%M"), "01")
        self.assertEqual(duration(timedelta(hours = 1), "%M"), "60")
        self.assertEqual(duration(timedelta(hours = 2), "%M"), "120")
        self.assertEqual(duration(timedelta(seconds = 17), "%o"), "0.00")
        self.assertEqual(duration(timedelta(seconds = 18), "%o"), "0.01")
        self.assertEqual(duration(timedelta(minutes = 6), "%o"), "0.10")
        self.assertEqual(duration(timedelta(minutes = 30), "%o"), "0.50")
        self.assertEqual(duration(timedelta(hours = 23, minutes = 30), "%o"), "23.50")
        self.assertEqual(duration(timedelta(hours = 24, minutes = 30), "%o"), "0.50")
        self.assertEqual(duration(timedelta(minutes = 30), "%O"), "0.50")
        self.assertEqual(duration(timedelta(hours = 23, minutes = 30), "%O"), "23.50")
        self.assertEqual(duration(timedelta(hours = 24, minutes = 30), "%O"), "24.50")
        self.assertEqual(duration(timedelta(days = 0), "%D"), "0")
        self.assertEqual(duration(timedelta(days = 1), "%D"), "1")
        
    def test_complex(self):
        self.assertEqual(duration(timedelta(hours = 26, minutes = 45), "%h %m %H %o %O"), "2 45 26 2.75 26.75")
    
    def test_rounding_simple(self):
        self.assertEqual(duration(timedelta(seconds = 29), "%m"), "00")
        self.assertEqual(duration(timedelta(seconds = 30), "%m"), "01")
        self.assertEqual(duration(timedelta(seconds = 29), "%M"), "00")
        self.assertEqual(duration(timedelta(seconds = 30), "%M"), "01")
        self.assertEqual(duration(timedelta(minutes = 29), "%h"), "0")
        self.assertEqual(duration(timedelta(minutes = 30), "%h"), "1")
        self.assertEqual(duration(timedelta(minutes = 29), "%H"), "0")
        self.assertEqual(duration(timedelta(minutes = 30), "%H"), "1")
        self.assertEqual(duration(timedelta(hours = 11), "%D"), "0")
        self.assertEqual(duration(timedelta(hours = 12), "%D"), "1")
    
    def test_rounding_complex(self):
        self.assertEqual(duration(timedelta(hours = 2, minutes = 30, seconds = 29), "%h:%m"), "2:30")
        self.assertEqual(duration(timedelta(hours = 2, minutes = 30, seconds = 30), "%h:%m"), "2:31")
        self.assertEqual(duration(timedelta(days = 1, hours = 11, minutes = 29), "%Dd %hh"), "1d 11h")
        self.assertEqual(duration(timedelta(days = 1, hours = 11, minutes = 30), "%Dd %hh"), "1d 12h")
        self.assertEqual(duration(timedelta(days = 1, hours = 11, minutes = 29, seconds = 29), "%Dd %hh %mm"), "1d 11h 29m")
        self.assertEqual(duration(timedelta(days = 1, hours = 11, minutes = 29, seconds = 30), "%Dd %hh %mm"), "1d 11h 30m")
        
test_suite = unittest.TestSuite()
test_suite.addTest(DurationTestCase("test_simple"))
test_suite.addTest(DurationTestCase("test_complex"))
test_suite.addTest(DurationTestCase("test_rounding_simple"))
test_suite.addTest(DurationTestCase("test_rounding_complex"))
runner = unittest.TextTestRunner()
runner.run(test_suite)
