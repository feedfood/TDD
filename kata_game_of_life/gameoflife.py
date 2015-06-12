import unittest

class myTestSuite(unittest.TestCase):
    def setup(self):
        pass

    def tearDown(self):
        pass

    def getNeighbors(self, matrix, center):
	count=0
	for x,row in enumerate(matrix):
	    for y,cell in enumerate(row):
		if(cell==1 and not(x==center[0] and y==center[1])):
		    count+=1    
        return count 

    def test_3x3x3_return_8(self):
	matrix=((1,1,1),(1,1,1),(1,1,1))
	center=(1,1)
        self.assertEqual(self.getNeighbors(matrix,center), 8)

if __name__ == "__main__":
    unittest.main()
