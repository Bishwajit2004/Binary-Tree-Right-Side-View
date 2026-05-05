# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import List, Optional

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # Count length
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next

        part_size = n // k
        extra = n % k

        result = []
        curr = head

        for i in range(k):
            part_head = curr
            size = part_size + (1 if i < extra else 0)

            # Move to the end of this part
            for _ in range(size - 1):
                if curr:
                    curr = curr.next

            # Cut the part
            if curr:
                next_part = curr.next
                curr.next = None
                curr = next_part

            result.append(part_head)

        return result
