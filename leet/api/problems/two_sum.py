class TwoSum:
    NOT_FOUND = "No solution found"
    LEET = "https://leetcode.com/problems/two-sum/"
    PLACE_THEO_SOLVED = "Criteo inteview August 27, 2020"

    def brute(self, numbers, target):
        """
            Complexity of O(N logN) most likely. Depends on how python does item in list.
        """
        for i, num in enumerate(numbers):
            if target - num in numbers:
                return [i, numbers.index(target - num)]

        return self.NOT_FOUND

    def outside_in(self, numbers, target):
        """
            Complexity of O(N), but doesn't handle unsorted, or negative numbers.
        """
        start = 0
        end = len(numbers) - 1
        potential_target = numbers[start] + numbers[end]

        while end != start:
            if potential_target == target:
                break
            elif potential_target > target:
                end -= 1
            else:
                start += 1
            potential_target = numbers[start] + numbers[end]
        else:
            # condition is false now, meaning no solution found
            return self.NOT_FOUND
        return [start, end]

    def trash_memory(self, numbers, target):
        """
            Complexity of O(N), handles unsorted, sorted, and negatives, but uses O(N^2)? memory as well.
        """
        cache = {}
        for i, num in enumerate(numbers):
            if cache.get(num) is not None:
                return [cache.get(num), i]
            cache[target - num] = i
        return self.NOT_FOUND
