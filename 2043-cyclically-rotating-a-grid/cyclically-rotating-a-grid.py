from typing import List

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        layers = min(m, n) // 2

        for layer in range(layers):
            top, bottom = layer, m - 1 - layer
            left, right = layer, n - 1 - layer

            vals = []

            # top row
            for c in range(left, right + 1):
                vals.append(grid[top][c])

            # right column
            for r in range(top + 1, bottom):
                vals.append(grid[r][right])

            # bottom row
            for c in range(right, left - 1, -1):
                vals.append(grid[bottom][c])

            # left column
            for r in range(bottom - 1, top, -1):
                vals.append(grid[r][left])

            shift = k % len(vals)
            rotated = vals[shift:] + vals[:shift]

            idx = 0

            # write top row
            for c in range(left, right + 1):
                grid[top][c] = rotated[idx]
                idx += 1

            # write right column
            for r in range(top + 1, bottom):
                grid[r][right] = rotated[idx]
                idx += 1

            # write bottom row
            for c in range(right, left - 1, -1):
                grid[bottom][c] = rotated[idx]
                idx += 1

            # write left column
            for r in range(bottom - 1, top, -1):
                grid[r][left] = rotated[idx]
                idx += 1

        return grid
