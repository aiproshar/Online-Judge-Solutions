# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return head

        current = head

        while current.next is not None:
            # Is it a duplicate
            if current.val == current.next.val:
                # Unlink the next dupe
                current.next = current.next.next
            else:
                # move forward
                current = current.next
        return head
# Time Complexity: O(n)
# Space: O(1), inplace modify