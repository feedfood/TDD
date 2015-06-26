import unittest

class myTestSuite(unittest.TestCase):
    def setup(self):
        pass

    def tearDown(self):
        pass

    def wrap(self, s, length):
        if( s == None):
            return "";
        return s; 

    def testWrap_Null_Returns_Empty(self):
        self.assertEqual(self.wrap(None,10),"")

    def testWrap_Empty_Returns_Empty(self):
        self.assertEqual(self.wrap("",10),"")

    def testWrap_OneShortWord_Not_Wrap(self):
        self.assertEqual(self.wrap("word",10),"word")

if __name__ == "__main__":
    unittest.main()
