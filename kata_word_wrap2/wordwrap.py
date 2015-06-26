import unittest

class myTestSuite(unittest.TestCase):
    def setup(self):
        pass

    def tearDown(self):
        pass

    def wrap(self, s, length):
        return None

    def testWrapNullReturnsEmptyString(self):
        self.assertEqual(self.wrap(None,10),"")

if __name__ == "__main__":
    unittest.main()
