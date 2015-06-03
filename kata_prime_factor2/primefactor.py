import unittest

class myTestSuite(unittest.TestCase):
    def setup(self):
        pass

    def tearDown(self):
        pass

    def prime(self, number):
	if(number%2==0 and number/2!=1): #return 2xA if number is 2 multiplys prime number
	    return [2] + (self.prime(number/2)) # return 2x2...xA if number is 2^n multiplys prime number
	if(number%3==0 and number/3!=1): #return 3xA if number is 3 multiplys prime number
	    return [3] + (self.prime(number/3)) # return 3x3...xA if number is 3^n multiplys prime number
	if(number>=2): #return prime number if number is prime
	    return [number]
	return [] #return empty if number <= 1

    def test_1_return_empty(self):
        self.assertEqual(self.prime(1), [])

    def test_2_return_2(self):
        self.assertEqual(self.prime(2), [2])

    def test_3_return_3(self):
        self.assertEqual(self.prime(3), [3])

    def test_4_return_2x2(self):
        self.assertEqual(self.prime(4), [2,2])

    def test_6_return_2x3(self):
        self.assertEqual(self.prime(6), [2,3])

    def test_8_return_2x2x2(self):
        self.assertEqual(self.prime(8), [2,2,2])

    def test_9_return_3x3(self):
        self.assertEqual(self.prime(9), [3,3])

if __name__ == "__main__":
    unittest.main()
