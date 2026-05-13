from typing import List

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        m = len(queries)

        def can_make_zero(k: int) -> bool:
            diff = [0] * (n + 1)

            for i in range(k):
                l, r, val = queries[i]
                diff[l] += val
                if r + 1 < n:
                    diff[r + 1] -= val

            total = 0
            for i in range(n):
                total += diff[i]
                if total < nums[i]:
                    return False
            return True

        if not can_make_zero(m):
            return -1

        lo, hi = 0, m
        while lo < hi:
            mid = (lo + hi) // 2
            if can_make_zero(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo
