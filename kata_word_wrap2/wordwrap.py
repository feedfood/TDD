import unittest

class myTestSuite(unittest.TestCase):
    def setup(self):
        pass

    def tearDown(self):
        pass

    def breakWords(self,result, ss,start,end):
        return result + ss[:start] + "\n", ss[end:]

    def wrap(self, s, length):
        if( s == None):
            return "";
            
        if(length < 1):
            raise IndexError
            
        result = ""
        ss = s
        while(len(ss)>length):
            spacePos = ss[:length].rfind(" ")
            if(spacePos>=0):
                result,ss = self.breakWords(result,ss,spacePos,spacePos+1)
            else:
                result,ss = self.breakWords(result,ss,length,length)
                
        result += ss
        return result

    def testWrap_Null_Returns_Empty(self):
        self.assertEqual(self.wrap(None,10),"")

    def testWrap_Empty_Returns_Empty(self):
        self.assertEqual(self.wrap("",10),"")

    def testWrap_OneShortWord_Not_Wrap(self):
        self.assertEqual(self.wrap("word",10),"word")
        
    def testWrap_OneLongWord_Wrap(self):
        self.assertEqual(self.wrap("longword",5),"longw\nord")        

    def testWrap_OneVeryLongWord_Wrap(self):
        self.assertEqual(self.wrap("verylongword",5),"veryl\nongwo\nrd")        

    def testWrap_TwoWords_Wrap(self):
        self.assertEqual(self.wrap("word wrap",6),"word\nwrap")
       
    def testWrap_ThreeWords_Wrap(self):
        self.assertEqual(self.wrap("word word wrap",6),"word\nword\nwrap")        

    def testWrap_ThreeWords_Wrap_at_second_space(self):
        self.assertEqual(self.wrap("word wrap here",10),"word wrap\nhere")
        
    def testWrap_length_less_than_1(self):
        with self.assertRaises(IndexError):
            self.wrap("xxx",-1)

if __name__ == "__main__":
    unittest.main()
