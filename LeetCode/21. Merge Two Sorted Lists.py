# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# simple loop and exhaust
# dummy head to support loop invariant
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        if list1 is None and list2 is None:
            return None
        head = ListNode()

        current = head

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
                current = current.next
            else:
                current.next = list2
                list2 = list2.next
                current = current.next
        if list1 is not None:
            current.next = list1
        if list2 is not None:
            current.next = list2
        return head.next

# Time Complexity: O(n)
# Space Complexity: O(1) no extra space