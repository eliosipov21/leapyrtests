import unittest
import leapyr 

class testCaseAdd(unittest.TestCase):
    def test_leap1(self):
        result = leapyr.leapyear(1600)
        self.assertEqual(result, True)
    def test_leap2(self):
        result2 = leapyr.leapyear(2018)
        self.assertEqual(result2, False)
    def test_leap3(self):
        result3 = leapyr.leapyear(99999999)
        self.assertEqual(result3, False)
    def test_leap4(self):
        result4 = leapyr.leapyear(0)
        self.assertEqual(result4, False)
    def test_leap5(self):
        result5 = leapyr.leapyear(-6)
        self.assertEqual(result5, False)
    

if __name__ == '__main__':
    unittest.main()