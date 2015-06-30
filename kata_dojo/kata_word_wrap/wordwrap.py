import unittest

class myTestSuite(unittest.TestCase):
    def setup(self):
        pass

    def tearDown(self):
        pass

#    def wrap(self,s,length):
#        if length < 1:
#            raise IndexError
#        if s is None:
#            return ""
#        if len(s) <= length:
#            return s
#        else:
#            space = s[:length].rfind(" ")
#            if space >= 0:
#                return s[:space] + "\n" + self.wrap(s[space+1:].lstrip(),length)
#            else:
#                return s[:length]+ "\n" + self.wrap(s[length:].lstrip(),length)
#

#    def wrap(self,s,length):
#        if length < 1:
#            raise IndexError
#        if s is None:
#            return ""
#        result = ""
#        while len(s) > length:
#            space = s[:length].rfind(" ")
#            if space >= 0:
#                result += s[:space] + "\n"
#                s = s[space+1:].lstrip()
#            else:
#                result += s[:length]+ "\n"
#                s = s[length:].lstrip()
#
#        return result + s
#
    def breakBetween(self, s, start, end, length):
        return s[:start] + "\n" + self.wrap(s[end:].lstrip(), length)

    def wrap(self, s, length):
        if length < 1:
            raise IndexError
        if s is None:
            return ""
        if len(s) <= length:
            return s
        else:
            space = s[:length].rfind(" ")
            if space >= 0:
                return self.breakBetween(s, space, space+1, length)
            else:
                return self.breakBetween(s,length,length,length)

    def testWrapNullReturnsEmptyString(self):
        self.assertEqual(self.wrap(None,10),"")

    def testWrapEmptyReturnsEmptyString(self):
        self.assertEqual(self.wrap("",10),"")
    
    def testLengthLessThanOneShouldThrowInvalidArgument(self):
        with self.assertRaises(IndexError):
            self.wrap("xxx",0)

    def testOneShortWordDoesNotWrap(self):
        self.assertEqual(self.wrap("word",10),"word")

    def testWordLongerThanLengthBreaksAtLength(self):
        self.assertEqual(self.wrap("longword",4),"long\nword")
        self.assertEqual(self.wrap("longerword",6),"longer\nword")
       
    def testWordLongerThanTwiceLengthShouldBreakTwice(self):
        self.assertEqual(self.wrap("verylongword",4),"very\nlong\nword")

    def testTwoWordsLongerThanLimitShouldWrap(self):
        self.assertEqual(self.wrap("word word",6),"word\nword")
        self.assertEqual(self.wrap("word wrap",6),"word\nwrap")
        self.assertEqual(self.wrap("word wrap wrap",6),"word\nwrap\nwrap")

    def testThreeWordsJustOverTheLimitShouldWrapAtSecondWord(self):
        self.assertEqual(self.wrap("word word word",11),"word word\nword")
        
    def testTwoWordsTheFirstEndingAtTheLimit(self):
        self.assertEqual(self.wrap("word word", 4), "word\nword")
        self.assertEqual(self.wrap("word  word", 4), "word\nword")
     
    def testTwoWordsTheFirstEndingAtTheLimit2(self):
        self.assertEqual(self.wrap("word word",5), "word\nword")
        self.assertEqual(self.wrap("word  word",5), "word\nword")

#    def testTwoWordsTheFirstEndingAtFirstWord(self):
#        self.assertEqual(self.wrap("word word",2),"wo\nrd\nwo\nrd")

if __name__ == "__main__":
    unittest.main()
