"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        a = [head]

        while a[-1].next:
            a.append(a[-1].next)

        if len(a) - n == 0:
            head = head.next
        else:
            a[-n-1].next = a[-n].next
        return head
