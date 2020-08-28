from django.test import TestCase

from leet.api.problems.two_sum import TwoSum


class TestTwoSum(TestCase):
    def setUp(self):
        self.two_sum = TwoSum()

    def test_outside_in(self):
        numbers = [0, 1, 4, 6, 30, 222, 500, 654, 699, 999]
        numbers_unsorted = [0, 1, 4, 6, 30, 222, 500, 654, 699, 999, 0]

        self.assertEqual([3, 7], self.two_sum.outside_in(numbers, 660))

        self.assertEqual([1, 9], self.two_sum.outside_in(numbers, 1000))

        self.assertEqual("No solution found", self.two_sum.outside_in(numbers, 5000))

        self.assertEqual(
            "No solution found", self.two_sum.outside_in(numbers_unsorted, 660)
        )

    def test_trash_memory(self):
        numbers = [0, 1, 4, 6, 30, 222, 500, 654, 699, 999]
        numbers_unsorted = [0, 1, 4, 6, 30, 222, 500, 654, 699, 999, 0]
        numbers_with_negatives = [4, 6, -5000, 222, -33, -5, 500, 654, -1]

        self.assertEqual([3, 7], self.two_sum.trash_memory(numbers, 660))

        self.assertEqual([1, 9], self.two_sum.trash_memory(numbers, 1000))

        self.assertEqual("No solution found", self.two_sum.trash_memory(numbers, 5000))

        self.assertEqual([3, 7], self.two_sum.trash_memory(numbers_unsorted, 660))

        self.assertEqual([4, 8], self.two_sum.trash_memory(numbers_with_negatives, -34))

        self.assertEqual(
            [2, 3], self.two_sum.trash_memory(numbers_with_negatives, -4778)
        )

    def test_brute(self):
        numbers = [0, 1, 4, 6, 30, 222, 500, 654, 699, 999]
        numbers_unsorted = [0, 1, 4, 6, 30, 222, 500, 654, 699, 999, 0]
        numbers_with_negatives = [4, 6, -5000, 222, -33, -5, 500, 654, -1]

        self.assertEqual([3, 7], self.two_sum.brute(numbers, 660))

        self.assertEqual([1, 9], self.two_sum.brute(numbers, 1000))

        self.assertEqual("No solution found", self.two_sum.brute(numbers, 5000))

        self.assertEqual([3, 7], self.two_sum.brute(numbers_unsorted, 660))

        self.assertEqual([4, 8], self.two_sum.brute(numbers_with_negatives, -34))

        self.assertEqual([2, 3], self.two_sum.brute(numbers_with_negatives, -4778))

    def test_multiple(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        target = 10

        expected = [[3, 5], [2, 6], [1, 7], [0, 8]]

        self.assertEqual(expected, self.two_sum.multiple_trash_memory(numbers, target))

        numbers = [19, 2, 13, -400, 5, 410, -3, 8, -9]

        self.assertEqual(expected, self.two_sum.multiple_trash_memory(numbers, target))
