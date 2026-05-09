from typing import List
import heapq

class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        m, n = len(values), len(values[0])
        heap = []

        # Start with the rightmost item from each shop
        for i in range(m):
            heapq.heappush(heap, (values[i][n - 1], i, n - 1))

        day = 1
        ans = 0

        while heap:
            val, i, j = heapq.heappop(heap)
            ans += val * day
            day += 1

            # Reveal the next item to the left in the same shop
            if j > 0:
                heapq.heappush(heap, (values[i][j - 1], i, j - 1))

        return ans
