from typing import List

class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return 0

        # pref[col][k] = sum of grid[0..k-1][col]
        pref = [[0] * (n + 1) for _ in range(n)]
        for col in range(n):
            for row in range(n):
                pref[col][row + 1] = pref[col][row] + grid[row][col]

        def gain(col: int, left: int, cur: int, right: int) -> int:
            top = max(left, right)
            if top <= cur:
                return 0
            return pref[col][top] - pref[col][cur]

        # Initialize with column 0 contribution, using virtual left height = 0
        dp = [[-10**30] * (n + 1) for _ in range(n + 1)]
        for h0 in range(n + 1):
            for h1 in range(n + 1):
                dp[h0][h1] = gain(0, 0, h0, h1)

        # Process middle columns
        for col in range(1, n - 1):
            ndp = [[-10**30] * (n + 1) for _ in range(n + 1)]
            P = pref[col]

            for b in range(n + 1):
                # prefix max of dp[a][b]
                pref_max = [-10**30] * (n + 1)
                best = -10**30
                for a in range(n + 1):
                    best = max(best, dp[a][b])
                    pref_max[a] = best

                # suffix max of dp[a][b] + max(0, P[a] - P[b])
                suff_max = [-10**30] * (n + 2)
                best = -10**30
                for a in range(n, -1, -1):
                    extra = P[a] - P[b] if a > b else 0
                    best = max(best, dp[a][b] + extra)
                    suff_max[a] = best

                for c in range(n + 1):
                    # Case 1: a <= c, then max(a, c) = c
                    add1 = (P[c] - P[b]) if c > b else 0
                    cand1 = pref_max[c] + add1

                    # Case 2: a > c, then max(a, c) = a
                    cand2 = suff_max[c + 1] if c < n else -10**30

                    ndp[b][c] = max(cand1, cand2)

            dp = ndp

        # Finalize last column with virtual right height = 0
        ans = 0
        for a in range(n + 1):
            for b in range(n + 1):
                ans = max(ans, dp[a][b] + gain(n - 1, a, b, 0))

        return ans
