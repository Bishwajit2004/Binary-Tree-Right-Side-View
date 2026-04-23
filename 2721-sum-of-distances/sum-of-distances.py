from collections import defaultdict
from typing import List

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        groups = defaultdict(list)
        for i, x in enumerate(nums):
            groups[x].append(i)

        n = len(nums)
        ans = [0] * n

        for pos in groups.values():
            k = len(pos)
            if k == 1:
                continue

            prefix = [0] * (k + 1)
            for i in range(k):
                prefix[i + 1] = prefix[i] + pos[i]

            total = prefix[k]
            for t, p in enumerate(pos):
                left = t * p - prefix[t]
                right = (total - prefix[t + 1]) - (k - 1 - t) * p
                ans[p] = left + right

        return ans
