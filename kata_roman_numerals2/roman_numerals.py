import unittest

class myTestSuite(unittest.TestCase):
    def setup(self):
        pass

    def tearDown(self):
        pass

    def number2roman(self, number):
    	if(number==4):
	    return "IV"
    	if(number==9):
	    return "IX"
    	preset_roman = {1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}
	keys = preset_roman.keys()
	keys.sort()
	for key in keys:
	    if(number-key>=0 and number-key<=3):
		return preset_roman[key].ljust(number-key+1,"I")
	return "" 

    def test_0_return_empty(self):
        self.assertEqual(self.number2roman(0), "")

    def test__1_return_empty(self):
        self.assertEqual(self.number2roman(-1), "")

    def test_1_return_I(self):
        self.assertEqual(self.number2roman(1), "I")

    def test_5_return_V(self):
        self.assertEqual(self.number2roman(5), "V")

    def test_10_return_X(self):
        self.assertEqual(self.number2roman(10), "X")

    def test_50_return_L(self):
        self.assertEqual(self.number2roman(50), "L")

    def test_100_return_C(self):
        self.assertEqual(self.number2roman(100), "C")
    
    def test_500_return_C(self):
        self.assertEqual(self.number2roman(500), "D")

    def test_1000_return_M(self):
        self.assertEqual(self.number2roman(1000), "M")

    def test_2_return_II(self):
        self.assertEqual(self.number2roman(2), "II")

    def test_3_return_III(self):
        self.assertEqual(self.number2roman(3), "III")

    def test_6_return_VI(self):
        self.assertEqual(self.number2roman(6), "VI")

    def test_7_return_VII(self):
        self.assertEqual(self.number2roman(7), "VII")

    def test_4_return_IV(self):
        self.assertEqual(self.number2roman(4), "IV")

    def test_9_return_IX(self):
        self.assertEqual(self.number2roman(9), "IX")

if __name__ == "__main__":
    unittest.main()
