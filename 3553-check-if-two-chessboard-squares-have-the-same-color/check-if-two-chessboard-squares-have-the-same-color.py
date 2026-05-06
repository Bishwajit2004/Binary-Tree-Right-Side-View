class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        def color(coord: str) -> int:
            return (ord(coord[0]) - ord('a') + int(coord[1])) % 2

        return color(coordinate1) == color(coordinate2)
