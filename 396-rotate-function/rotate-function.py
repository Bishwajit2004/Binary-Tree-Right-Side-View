from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        total = sum(nums)
        current = sum(i * num for i, num in enumerate(nums))
        best = current
        n = len(nums)

        for i in range(n - 1, 0, -1):
            current += total - n * nums[i]
            best = max(best, current)

        return best
