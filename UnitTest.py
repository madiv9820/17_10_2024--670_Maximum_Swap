from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__testCases = {
            1: {'num': 2736, 'output': 7236},
            2: {'num': 9973, 'output': 9973},
            3: {'num': 12, 'output': 21},
            4: {'num': 98368, 'output': 98863},
            5: {'num': 1993, 'output': 9913}
        }

        self.__obj = Solution()

        return super().setUp()

    @timeout(0.5)
    def test_Case1(self):
        num, output = self.__testCases[1].values()
        result = self.__obj.maximumSwap(num = num)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_Case2(self):
        num, output = self.__testCases[2].values()
        result = self.__obj.maximumSwap(num = num)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)
    
    @timeout(0.5)
    def test_Case3(self):
        num, output = self.__testCases[3].values()
        result = self.__obj.maximumSwap(num = num)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_Case4(self):
        num, output = self.__testCases[4].values()
        result = self.__obj.maximumSwap(num = num)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_Case5(self):
        num, output = self.__testCases[5].values()
        result = self.__obj.maximumSwap(num = num)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()