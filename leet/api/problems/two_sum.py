class TwoSum:
    NOT_FOUND = "No solution found"
    DESCRIPTION = """

    """

    def brute(self, numbers, target):
        return self.NOT_FOUND

    def outside_in(self, numbers, target):
        start = len(numbers) - 1
        end = 0
        potential_target = numbers[start] + numbers[end]
        while end != start:
            if potential_target == target:
                break
            elif potential_target > target:
                end -= 1
            else:
                start += 1
        else:
            # condition is false now, meaning no solution found
            return self.NOT_FOUND
        return [start, end]

    def thrash_memory(self, numbers, target):
        pass
