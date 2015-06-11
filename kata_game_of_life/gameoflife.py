import unittest

class myTestSuite(unittest.TestCase):
    def setup(self):
        pass

    def tearDown(self):
        pass

    def play(self, number):
        return None 

    def test_1_return_1(self):
        self.assertEqual(self.speak(1), "1")

if __name__ == "__main__":
    unittest.main()
