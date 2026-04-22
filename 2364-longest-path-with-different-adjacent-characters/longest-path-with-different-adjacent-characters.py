from typing import List
from collections import defaultdict

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        tree = defaultdict(list)
        n = len(parent)

        for i in range(1, n):
            tree[parent[i]].append(i)

        self.ans = 1

        def dfs(node: int) -> int:
            longest = 0
            second_longest = 0

            for child in tree[node]:
                child_path = dfs(child)

                if s[child] == s[node]:
                    continue

                if child_path > longest:
                    second_longest = longest
                    longest = child_path
                elif child_path > second_longest:
                    second_longest = child_path

            self.ans = max(self.ans, longest + second_longest + 1)
            return longest + 1

        dfs(0)
        return self.ans
