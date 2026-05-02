from typing import List


class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.LOG = n.bit_length()
        self.up = [[-1] * n for _ in range(self.LOG)]
        self.up[0] = parent[:]

        for j in range(1, self.LOG):
            for i in range(n):
                prev = self.up[j - 1][i]
                if prev != -1:
                    self.up[j][i] = self.up[j - 1][prev]

    def getKthAncestor(self, node: int, k: int) -> int:
        bit = 0
        while k > 0 and node != -1:
            if k & 1:
                node = self.up[bit][node]
            k >>= 1
            bit += 1
        return node
