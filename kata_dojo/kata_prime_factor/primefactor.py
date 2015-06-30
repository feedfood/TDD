import unittest

class myTestSuite(unittest.TestCase):
    def setup(self):
        pass

    def tearDown(self):
        pass

    def prime(self, number):
        result = []
        candidate = 2

        while(candidate < number):
            while(number % candidate == 0):
                result.append(candidate)
                number = number / candidate
            candidate += 1

        if(number > 1):
            result.append(number)

        return result

    def test_1_return_empty(self):
        self.assertEqual(self.prime(1), [])

    def test_2_return_2(self):
        self.assertEqual(self.prime(2), [2])

    def test_3_return_3(self):
        self.assertEqual(self.prime(3), [3])

    def test_4_return_2_2(self):
        self.assertEqual(self.prime(4), [2, 2])

    def test_6_return_2_3(self):
        self.assertEqual(self.prime(6), [2, 3])

    def test_8_return_2_2_2(self):
        self.assertEqual(self.prime(8), [2, 2, 2])

    def test_9_return_3_3(self):
        self.assertEqual(self.prime(9), [3, 3])

    def test_100_return_2x2x5x5(self):
        self.assertEqual(self.prime(100), [2,2,5,5])
if __name__ == "__main__":
    unittest.main()
