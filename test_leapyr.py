import unittest
import leapyr 

class testCaseAdd(unittest.TestCase):
    def test_leap1(self):
        result = leapyr.leapyear(1600)
        self.assertEqual(result, True)
    def test_leap2(self):
        result2 = leapyr.leapyear(2018)
        self.assertEqual(result2, False)

if __name__ == '__main__':
    unittest.main()