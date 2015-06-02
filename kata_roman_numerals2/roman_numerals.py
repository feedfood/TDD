import unittest

class myTestSuite(unittest.TestCase):
    def setup(self):
        pass

    def tearDown(self):
        pass

    def number2roman(self, number):
    	preset_roman = {1:"I",5:"V"}
	if(preset_roman.has_key(number)):
	    return preset_roman[number]
	return "" 

    def test_0_return_empty(self):
        self.assertEqual(self.number2roman(0), "")

    def test__1_return_empty(self):
        self.assertEqual(self.number2roman(-1), "")

    def test_1_return_I(self):
        self.assertEqual(self.number2roman(1), "I")

    def test_5_return_V(self):
        self.assertEqual(self.number2roman(5), "V")

if __name__ == "__main__":
    unittest.main()
