import unittest

class myTestSuite(unittest.TestCase):
    def setup(self):
        pass

    def tearDown(self):
        pass

    def speak(self, number):
	result = "" 
	if(number%3==0):
	    result += "fizz"
	if(number%5==0):
	    result += "buzz"
	if(result==""):
	    result = str(number)
        return result 

    def test_1_return_1(self):
        self.assertEqual(self.speak(1), "1")

    def test_3_return_fizz(self):
        self.assertEqual(self.speak(3), "fizz")

    def test_5_return_buzz(self):
        self.assertEqual(self.speak(5), "buzz")

    def test_15_return_fizzbuzz(self):
        self.assertEqual(self.speak(15), "fizzbuzz")

if __name__ == "__main__":
    unittest.main()
