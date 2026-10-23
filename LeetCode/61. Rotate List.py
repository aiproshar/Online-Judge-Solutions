# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:


        if head is None or head.next is None:
            return head

        tail = head
        len_ = 1
        while tail.next is not None:
            tail = tail.next
            len_ += 1
        # make it circular first
        tail.next = head
        k = k % len_
        cut_point = len_ - k - 1
        current = head
        while cut_point > 0:
            current = current.next
            cut_point -= 1
        head = current.next
        current.next = None
        return head
