# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Brute Force solution
# HashMap to store id of each object, in python default id tied to memory address
# Two nodes with same value will be different id
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        current = head
        while current is not None:
            if current in visited:
                return True
            else:
                visited.add(current)
                current = current.next
        return False
# Time complexity: O(n)
# Space complexity: O(n)


#--------------------- followup , can we do that in constant memory----------------

# important trick here is to not fall None dereference error, always think before accessing node.next, can node be null
# just think of this we will be fine
# This is known as: floyd's cycle detection algorithm

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow = head
        fast = head

        while slow is not None and fast is not None:
            slow = slow.next
            fast = fast.next
            if fast is None:
                return False
            fast = fast.next
            if slow == fast:
                return True
        return False
