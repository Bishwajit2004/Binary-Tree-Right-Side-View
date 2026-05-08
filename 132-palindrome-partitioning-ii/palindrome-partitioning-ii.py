class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [i for i in range(n)]  # worst case: cut before every char

        def expand(left: int, right: int):
            while left >= 0 and right < n and s[left] == s[right]:
                if left == 0:
                    dp[right] = 0
                else:
                    dp[right] = min(dp[right], dp[left - 1] + 1)
                left -= 1
                right += 1

        for i in range(n):
            expand(i, i)       # odd-length palindromes
            expand(i, i + 1)   # even-length palindromes

        return dp[-1]
