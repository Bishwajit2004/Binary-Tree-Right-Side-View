from bisect import bisect_right
from typing import List

class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        ans = []
        for x in queries:
            idx = bisect_right(nums, x)

            left = x * idx - prefix[idx]
            right = (prefix[n] - prefix[idx]) - x * (n - idx)

            ans.append(left + right)

        return ans
