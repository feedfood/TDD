import unittest

class myTestSuite(unittest.TestCase):
    def setup(self):
        pass

    def tearDown(self):
        pass

    def number2roman(self, number):
	if(number == 1):
	    return "I"
	return "" 

    def test_0_return_empty(self):
        self.assertEqual(self.number2roman(0), "")

    def test__1_return_empty(self):
        self.assertEqual(self.number2roman(-1), "")

    def test_1_return_I(self):
        self.assertEqual(self.number2roman(1), "I")

if __name__ == "__main__":
    unittest.main()
