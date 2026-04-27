from functools import lru_cache
from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        # A valid parentheses string must have even length
        if (m + n - 1) % 2 == 1:
            return False

        # Must start with '(' and end with ')'
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        @lru_cache(None)
        def dfs(r: int, c: int, balance: int) -> bool:
            if balance < 0:
                return False

            # pruning: even if all remaining chars were ')', can't close enough
            remaining = (m - 1 - r) + (n - 1 - c)
            if balance > remaining + 1:
                return False

            if r == m - 1 and c == n - 1:
                return balance == 0

            for nr, nc in ((r + 1, c), (r, c + 1)):
                if nr < m and nc < n:
                    nb = balance + (1 if grid[nr][nc] == '(' else -1)
                    if dfs(nr, nc, nb):
                        return True

            return False

        start_balance = 1  # grid[0][0] == '('
        return dfs(0, 0, start_balance)
