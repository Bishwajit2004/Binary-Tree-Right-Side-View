from typing import List
from collections import Counter

class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        freq = list(Counter(nums).values())
        m = len(quantity)
        size = 1 << m

        # sumq[mask] = total quantity needed by customers in mask
        sumq = [0] * size
        for mask in range(1, size):
            lsb = mask & -mask
            i = lsb.bit_length() - 1
            sumq[mask] = sumq[mask ^ lsb] + quantity[i]

        # dp[mask] = whether some processed frequencies can satisfy customers in mask
        dp = [False] * size
        dp[0] = True

        for f in freq:
            new_dp = dp[:]
            for mask in range(size):
                if not dp[mask]:
                    continue
                remain = ((size - 1) ^ mask)
                sub = remain
                while sub:
                    if sumq[sub] <= f:
                        new_dp[mask | sub] = True
                    sub = (sub - 1) & remain
            dp = new_dp

        return dp[size - 1]
