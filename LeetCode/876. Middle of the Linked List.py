# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


'''
Easy problem but with edge cases, but ultimately they don't create different branch
Odd vs Even, but if we start from imaginary sentinel, we all good
'''
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        slow = head
        fast = head.next
        while True:
            if fast.next is not None and fast.next.next is not None:
                fast = fast.next.next
                slow = slow.next
            else:
                break
        return slow.next
# Time Complexity: O(n)
# Space: O(1)