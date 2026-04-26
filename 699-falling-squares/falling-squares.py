from typing import List

class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        intervals = []  # (left, right, height)
        ans = []
        tallest = 0

        for left, side in positions:
            right = left + side
            base = 0

            for l, r, h in intervals:
                if max(left, l) < min(right, r):  # overlap
                    base = max(base, h)

            height = base + side
            intervals.append((left, right, height))

            tallest = max(tallest, height)
            ans.append(tallest)

        return ans
