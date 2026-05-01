from functools import lru_cache
from typing import List, Optional

# LeetCode provides the TreeNode class.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        @lru_cache(maxsize=None)
        def build(start: int, end: int):
            if start > end:
                return (None,)

            trees = []
            for root_val in range(start, end + 1):
                for left in build(start, root_val - 1):
                    for right in build(root_val + 1, end):
                        trees.append(TreeNode(root_val, left, right))
            return tuple(trees)

        return list(build(1, n))
