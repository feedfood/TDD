import unittest

class myTestSuite(unittest.TestCase):
    def setup(self):
        pass

    def tearDown(self):
        pass

    def number2roman(self, number):
	if(number<0):
	    return ""

	preset_roman = {0:"",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}
	if(preset_roman.has_key(number)):
	    return preset_roman[number]

	lastkey=0;
	keys = preset_roman.keys()
	keys.sort()
	for key in keys:
	    if( number-key<=3 and number-key>0):
		return preset_roman[key] + "".ljust(number-key,"I")
	    if( key-number==1):
		return "".rjust(1,"I") + preset_roman[key] 
	    if( key>number ):
	        return preset_roman[lastkey]+self.number2roman(number-lastkey)	
	    lastkey=key

	return preset_roman[lastkey]+self.number2roman(number-lastkey)	

    def test_0_return_empty(self):
        self.assertEqual(self.number2roman(0), "")

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

    def test_2_return_II(self):
        self.assertEqual(self.number2roman(2), "II")

    def test_3_return_III(self):
        self.assertEqual(self.number2roman(3), "III")

    def test_4_return_IV(self):
        self.assertEqual(self.number2roman(4), "IV")

    def test_6_return_VI(self):
        self.assertEqual(self.number2roman(6), "VI")

    def test_8_return_VIII(self):
        self.assertEqual(self.number2roman(8), "VIII")

    def test_14_return_XIV(self):
        self.assertEqual(self.number2roman(14), "XIV")

    def test_1000_return_M(self):
        self.assertEqual(self.number2roman(1000), "M")

    def test_1014_return_MXIV(self):
        self.assertEqual(self.number2roman(1014), "MXIV")

if __name__ == "__main__":
    unittest.main()
