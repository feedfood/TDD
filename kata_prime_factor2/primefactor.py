import unittest

class myTestSuite(unittest.TestCase):
    def setup(self):
        pass

    def tearDown(self):
        pass

    def prime(self, number):
	return [] 

    def test_1_return_empty(self):
        self.assertEqual(self.prime(1), [])

if __name__ == "__main__":
    unittest.main()
