import unittest

class myTestSuite(unittest.TestCase):
    def setup(self):
        pass

    def tearDown(self):
        pass

    def number2roman(self, number):
	if(number<0):
	    return "" 

	right_value = {1:"I",10:"X",100:"C"}
    	preset_roman = {0:"",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}
	keys = preset_roman.keys()
	keys.sort()
	lastkey=0
	for key in keys:
	    if(number-key>=0 and number-key<=3):
		return preset_roman[key]+"".ljust(number-key,"I")
	    if(key-number in right_value.keys()):
		return preset_roman[key].rjust(2,right_value[key-number])
	    if(key>number):
		return preset_roman[lastkey]+self.number2roman(number-lastkey)
	    lastkey=key

	return preset_roman[lastkey]+self.number2roman(number-lastkey)

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

    def test_14_return_XIV(self):
        self.assertEqual(self.number2roman(14), "XIV")

    def test_15_return_XV(self):
        self.assertEqual(self.number2roman(15), "XV")

    def test_40_return_XL(self):
        self.assertEqual(self.number2roman(40), "XL")

    def test_90_return_XC(self):
        self.assertEqual(self.number2roman(90), "XC")

    def test_1014_return_MXIV(self):
        self.assertEqual(self.number2roman(1014), "MXIV")

if __name__ == "__main__":
    unittest.main()
