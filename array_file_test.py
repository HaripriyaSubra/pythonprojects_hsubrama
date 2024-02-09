import unittest

import arraya_file


class ArrayFileTest(unittest.TestCase):
    def test_remove_duplicates(self):
        numbers = [1, 2, 3, 3, 5, 6, 2, 1]
        non_dup_array = arraya_file.remove_duplicates(numbers)
        print(len(non_dup_array))
        self.assertEqual(len(non_dup_array), 5)

    def test_sort_ascending(self):
        numbers = [56, 45, 23, 67, 34]
        sorted_array = arraya_file.sort_ascending(numbers)
        self.assertEqual(sorted_array, [23, 34, 45, 56, 67])

    def test_sort_descending(self):
        numbers = [56, 45, 23, 67, 34]
        sorted_array = arraya_file.sort_descending(numbers)
        self.assertEqual(sorted_array, [67, 56, 45, 34, 23])


if __name__ == '__main__':
    unittest.main()
