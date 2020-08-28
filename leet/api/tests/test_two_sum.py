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

        self.assertEqual("No solution found", self.two_sum.outside_in(numbers_unsorted, 660))

    def test_trash_memory(self):
        numbers = [0, 1, 4, 6, 30, 222, 500, 654, 699, 999]
        numbers_unsorted = [0, 1, 4, 6, 30, 222, 500, 654, 699, 999, 0]
        numbers_with_negatives = [0, 1, 4, 6, 30, -5000, 222, -33, -5, 500, 654, 699, 999, -1]

        self.assertEqual([3, 7], self.two_sum.trash_memory(numbers, 660))

        self.assertEqual([1, 9], self.two_sum.trash_memory(numbers, 1000))

        self.assertEqual("No solution found", self.two_sum.trash_memory(numbers, 5000))

        self.assertEqual([3, 7], self.two_sum.trash_memory(numbers_unsorted, 660))

        self.assertEqual([0, 7], self.two_sum.trash_memory(numbers_with_negatives, -33))

        self.assertEqual([5, 12], self.two_sum.trash_memory(numbers_with_negatives, -4001))

    def test_brute(self):
        numbers = [0, 1, 4, 6, 30, 222, 500, 654, 699, 999]
        numbers_unsorted = [0, 1, 4, 6, 30, 222, 500, 654, 699, 999, 0]
        numbers_with_negatives = [0, 1, 4, 6, 30, -5000, 222, -33, -5, 500, 654, 699, 999, -1]

        self.assertEqual([3, 7], self.two_sum.brute(numbers, 660))

        self.assertEqual([1, 9], self.two_sum.brute(numbers, 1000))

        self.assertEqual("No solution found", self.two_sum.brute(numbers, 5000))

        self.assertEqual([3, 7], self.two_sum.brute(numbers_unsorted, 660))

        self.assertEqual([0, 7], self.two_sum.brute(numbers_with_negatives, -33))

        self.assertEqual([5, 12], self.two_sum.brute(numbers_with_negatives, -4001))
