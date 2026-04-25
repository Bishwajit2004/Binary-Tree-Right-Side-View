from bisect import bisect_left
from typing import List

class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        L = 4 * side

        def perimeter_pos(x: int, y: int) -> int:
            if y == 0:
                return x                  # bottom
            if x == side:
                return side + y           # right
            if y == side:
                return 3 * side - x       # top
            return 4 * side - y           # left

        pos = sorted(perimeter_pos(x, y) for x, y in points)
        n = len(pos)

        def can(d: int) -> bool:
            if k * d > L:
                return False

            arr = pos + [x + L for x in pos]

            nxt = [2 * n] * (2 * n + 1)
            j = 0
            for i in range(2 * n):
                j = max(j, i + 1)
                while j < 2 * n and arr[j] - arr[i] < d:
                    j += 1
                nxt[i] = j

            LOG = 6  # enough because k <= 25
            up = [nxt[:]]
            for _ in range(1, LOG):
                prev = up[-1]
                cur = [2 * n] * (2 * n + 1)
                for i in range(2 * n + 1):
                    cur[i] = prev[prev[i]]
                up.append(cur)

            for start in range(n):
                cur = start
                steps = k - 1
                bit = 0
                while steps:
                    if steps & 1:
                        cur = up[bit][cur]
                    steps >>= 1
                    bit += 1

                if cur < start + n and arr[cur] - arr[start] <= L - d:
                    return True

            return False

        lo, hi = 0, side
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
