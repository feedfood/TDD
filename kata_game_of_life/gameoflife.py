import unittest

class myTestSuite(unittest.TestCase):
    def setup(self):
        pass

    def tearDown(self):
        pass

    def getNeighbors(self, matrix, center):
	count=0
	x_steps=(-1,0,1)
	y_steps=(-1,0,1)
	for x_step in x_steps:
	    for y_step in y_steps:
		x=center[0]+x_step
		y=center[1]+y_step
		if(x<0 or y<0):
		    continue
     	        if(x>3 or y>3):
		    continue
	        if(x==center[0] and y==center[1]):
		    continue
	        if(matrix[x][y]==1):
		    count+=1
        return count 

    def test_111x111x111_return_8(self):
	matrix=((1,1,1),(1,1,1),(1,1,1))
	center=(1,1)
        self.assertEqual(self.getNeighbors(matrix,center), 8)

    def test_000x010x000_return_0(self):
	matrix=((0,0,0),(0,1,0),(0,0,0))
	center=(1,1)
        self.assertEqual(self.getNeighbors(matrix,center), 0)

    def test_11111x11111x11111x11111x11111_return_24(self):
	matrix=((1,1,1,1,1),(1,1,1,1,1),(1,1,1,1,1),(1,1,1,1,1),(1,1,1,1,1))
	center=(2,2)
        self.assertEqual(self.getNeighbors(matrix,center), 8)

if __name__ == "__main__":
    unittest.main()
