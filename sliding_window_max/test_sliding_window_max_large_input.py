import time
import unittest
from sliding_window_max import sliding_window_max

class Test(unittest.TestCase):
    def test_sliding_window_max_large_input(self):
        arr = []
        k = 1000

        input_path = 'C:/Users/tiffa/Documents/git/cs-module-project-algorithms/sliding_window_max/data/input.txt'
        output_path = 'C:/Users/tiffa/Documents/git/cs-module-project-algorithms/sliding_window_max/data/output.txt'

        with open(input_path) as file:
            for line in file:
                arr.append(int(line.strip()))

        expected = []

        with open(output_path) as file:
            for line in file:
                expected.append(int(line.strip()))

        start_time = time.time()
        answer = sliding_window_max(arr, k)
        end_time = time.time()

        self.assertFalse((end_time - start_time) < 1)
        self.assertEqual(answer, expected)


if __name__ == '__main__':
    unittest.main()
