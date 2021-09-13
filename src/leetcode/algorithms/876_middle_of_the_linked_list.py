"""
https://leetcode.com/problems/middle-of-the-linked-list/
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middle_node1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # using an array
        a = [head]
        while a[-1].next:
            a.append(a[-1].next)

        return a[len(a) // 2]

    def middle_node2(self, head):
        # using fast and slow pointer
        # (fast meaning that it will arrive to the end twice as fast as the slow one)
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
