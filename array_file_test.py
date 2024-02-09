import unittest

import arraya_file


class ArrayFileTest(unittest.TestCase):
    def test_remove_duplicates(self):
        numbers = [1, 2, 3, 3, 5, 6, 2, 1]
        non_dup_array = arraya_file.remove_duplicates(numbers)
        print(len(non_dup_array))
        self.assertEqual(len(non_dup_array), 5)


if __name__ == '__main__':
    unittest.main()
