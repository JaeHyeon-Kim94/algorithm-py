# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
import collections
from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head:Optional[ListNode]) -> bool:
        q = collections.deque()
        curr = head

        while curr is not None:
            q.append(curr.val)
            curr = curr.next

        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
        return True
