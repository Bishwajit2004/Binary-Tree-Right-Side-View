from typing import List

class TrieNode:
    def __init__(self):
        self.child = [None, None]
        self.cnt = 0


class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        HIGH_BIT = 15  # since nums[i], high <= 2 * 10^4 < 2^15

        def count_less_than(limit: int) -> int:
            root = TrieNode()

            def insert(num: int) -> None:
                node = root
                for k in range(HIGH_BIT, -1, -1):
                    b = (num >> k) & 1
                    if not node.child[b]:
                        node.child[b] = TrieNode()
                    node = node.child[b]
                    node.cnt += 1

            def query(num: int) -> int:
                node = root
                ans = 0
                for k in range(HIGH_BIT, -1, -1):
                    if not node:
                        break

                    b = (num >> k) & 1
                    lb = (limit >> k) & 1

                    if lb == 1:
                        # take XOR bit 0 here, and continue with XOR bit 1
                        if node.child[b]:
                            ans += node.child[b].cnt
                        node = node.child[1 - b]
                    else:
                        # must keep XOR bit 0
                        node = node.child[b]
                return ans

            res = 0
            for num in nums:
                res += query(num)
                insert(num)
            return res

        return count_less_than(high + 1) - count_less_than(low)
