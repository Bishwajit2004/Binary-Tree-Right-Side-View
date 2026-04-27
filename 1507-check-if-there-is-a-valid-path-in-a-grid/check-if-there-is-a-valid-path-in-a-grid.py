from collections import deque
from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        # street type -> allowed directions
        # (dr, dc)
        dirs = {
            1: [(0, -1), (0, 1)],   # left, right
            2: [(-1, 0), (1, 0)],   # up, down
            3: [(0, -1), (1, 0)],   # left, down
            4: [(0, 1), (1, 0)],    # right, down
            5: [(0, -1), (-1, 0)],  # left, up
            6: [(0, 1), (-1, 0)],   # right, up
        }

        q = deque([(0, 0)])
        visited = {(0, 0)}

        while q:
            r, c = q.popleft()
            if r == m - 1 and c == n - 1:
                return True

            for dr, dc in dirs[grid[r][c]]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    # neighbor must connect back
                    if (-dr, -dc) in dirs[grid[nr][nc]]:
                        visited.add((nr, nc))
                        q.append((nr, nc))

        return False
