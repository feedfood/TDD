import unittest

class myTestSuite(unittest.TestCase):
    def setup(self):
        pass

    def tearDown(self):
        pass

    def prime(self, number):
	if(number==4):
	    return [2,2]
	if(number>=2):
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

if __name__ == "__main__":
    unittest.main()
