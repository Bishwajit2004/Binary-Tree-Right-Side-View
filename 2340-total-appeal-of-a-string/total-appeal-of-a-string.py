class Solution:
    def appealSum(self, s: str) -> int:
        last = {}
        n = len(s)
        total = 0

        for i, ch in enumerate(s):
            prev = last.get(ch, -1)
            total += (i - prev) * (n - i)
            last[ch] = i

        return total
