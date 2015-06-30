import unittest

class myTestSuite(unittest.TestCase):
    def setup(self):
        pass

    def tearDown(self):
        pass

    def prime(self, number):
	result=[]
	candidate=2
        while(candidate<number):
	    while(number%candidate==0):
                result.append(candidate)
	        number=number/candidate
	    candidate+=1
        if(number>1):	
	    result.append(number)
        return result 

    def test_1_return_empty(self):
        self.assertEqual(self.prime(1), [])

    def test_2_return_2(self):
        self.assertEqual(self.prime(2), [2])

    def test_3_return_3(self):
        self.assertEqual(self.prime(3), [3])

    def test_4_return_2x2(self):
        self.assertEqual(self.prime(4), [2,2])

    def test_8_return_2x2x2(self):
        self.assertEqual(self.prime(8), [2,2,2])

    def test_9_return_3x3(self):
        self.assertEqual(self.prime(9), [3,3])

if __name__ == "__main__":
    unittest.main()
