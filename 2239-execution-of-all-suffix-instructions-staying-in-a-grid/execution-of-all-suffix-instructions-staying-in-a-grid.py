class Solution:
    def executeInstructions(self, n: int, startPos: list[int], s: str) -> list[int]:
        m = len(s)
        ans = [0] * m

        for i in range(m):
            row, col = startPos
            count = 0

            for j in range(i, m):
                if s[j] == 'L':
                    col -= 1
                elif s[j] == 'R':
                    col += 1
                elif s[j] == 'U':
                    row -= 1
                else:
                    row += 1

                if row < 0 or row >= n or col < 0 or col >= n:
                    break

                count += 1

            ans[i] = count

        return ans
