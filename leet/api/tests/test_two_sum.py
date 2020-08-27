from django.test import TestCase

from leet.api.problems.two_sum import TwoSum


class TestTwoSum(TestCase):
    def setUp(self):
        self.two_sum = TwoSum()

    def test_outside_in(self):
        numbers = [0, 1, 4, 6, 30, 222, 500, 654, 699, 999]

        self.assertEqual([3, 7], self.two_sum.outside_in(numbers, 660))

        self.assertEqual([0, 0], self.two_sum.outside_in(numbers, 1000))

        self.assertEqual("No solutions found", self.two_sum.outside_in(numbers, 5000))
