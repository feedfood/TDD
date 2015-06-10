import unittest

class myTestSuite(unittest.TestCase):
    def setup(self):
        pass

    def tearDown(self):
        pass

    def speak(self, number):
        return str(number)

    def test_1_return_100(self):
        self.assertEqual(self.speak(1), "1")

if __name__ == "__main__":
    unittest.main()
