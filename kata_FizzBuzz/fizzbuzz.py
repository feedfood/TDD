import unittest

class myTestSuite(unittest.TestCase):
    def setup(self):
        pass

    def tearDown(self):
        pass

    def speak(self, number):
	if(number%3==0):
	    return "fizz"
        return str(number)

    def test_1_return_1(self):
        self.assertEqual(self.speak(1), "1")

    def test_3_return_fizz(self):
        self.assertEqual(self.speak(3), "fizz")

if __name__ == "__main__":
    unittest.main()
