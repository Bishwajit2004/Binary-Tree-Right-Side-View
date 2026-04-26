from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)

        for l, r, d in shifts:
            val = 1 if d == 1 else -1
            diff[l] += val
            diff[r + 1] -= val

        res = []
        curr = 0

        for i, ch in enumerate(s):
            curr += diff[i]
            offset = (ord(ch) - ord('a') + curr) % 26
            res.append(chr(ord('a') + offset))

        return "".join(res)
