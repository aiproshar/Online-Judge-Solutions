# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        l3 = ListNode(None, None)
        head = l3
        carry = False


        while l1 or l2:
            sum_ = 0
            if l1:
                sum_ += l1.val
                l1 = l1.next
            if l2:
                sum_ += l2.val
                l2 = l2.next
            if carry:
                sum_ += 1
                carry = False
            if sum_ > 9:
                carry = True
                sum_ = sum_ % 10
            l3.next = ListNode(sum_)
            l3 = l3.next
        if carry:
            l3.next = ListNode(1, None)
        return head.next