import unittest

class myTestSuite(unittest.TestCase):
    def setup(self):
        pass

    def tearDown(self):
        pass

    def prime(self, number):
	candidate=2
	while(candidate<number):
	    if(number%candidate==0 and number/candidate!=1): 
		return [candidate] + (self.prime(number/candidate)) 
	    candidate+=1
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

    def test_100_return_2x2x5x5(self):
        self.assertEqual(self.prime(100), [2,2,5,5])

if __name__ == "__main__":
    unittest.main()
