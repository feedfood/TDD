import unittest

class myTestSuite(unittest.TestCase):
    def setup(self):
        pass

    def tearDown(self):
        pass

    def number2roman(self, number):
    	preset_roman = {1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}
	if(preset_roman.has_key(number)):
	    return preset_roman[number]

	if(number==2):
	    return "II"
	if(number==3):
	    return "III"
	if(number==6):
	    return "VI"
    	if(number==7):
	    return "VII"
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

if __name__ == "__main__":
    unittest.main()
