import unittest

class myTestSuite(unittest.TestCase):
    def setup(self):
        pass

    def tearDown(self):
        pass

    def number2roman(self, number):
	return None

    def test_0_return_empty(self):
        self.assertEqual(self.number2roman(0), "")

if __name__ == "__main__":
    unittest.main()
