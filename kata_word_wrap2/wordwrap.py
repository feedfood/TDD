import unittest

class myTestSuite(unittest.TestCase):
    def setup(self):
        pass

    def tearDown(self):
        pass

    def wrap(self, s, length):
        if( s == None):
            return "";
            
        if(len(s)<=length):
            return s;
            
        return s[:length] + "\n" + s[length:] 

    def testWrap_Null_Returns_Empty(self):
        self.assertEqual(self.wrap(None,10),"")

    def testWrap_Empty_Returns_Empty(self):
        self.assertEqual(self.wrap("",10),"")

    def testWrap_OneShortWord_Not_Wrap(self):
        self.assertEqual(self.wrap("word",10),"word")
        
    def testWrap_OneLongWord_Wrap(self):
        self.assertEqual(self.wrap("longword",5),"longw\nord")        

if __name__ == "__main__":
    unittest.main()
