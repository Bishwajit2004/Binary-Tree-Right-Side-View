from typing import List

class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])

        # Step 1: let stones fall to the right in each row
        for row in boxGrid:
            empty = n - 1  # rightmost available position for a stone
            for col in range(n - 1, -1, -1):
                if row[col] == '*':
                    empty = col - 1
                elif row[col] == '#':
                    row[col] = '.'
                    row[empty] = '#'
                    empty -= 1

        # Step 2: rotate 90 degrees clockwise
        rotated = [[None] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                rotated[j][m - 1 - i] = boxGrid[i][j]

        return rotated
