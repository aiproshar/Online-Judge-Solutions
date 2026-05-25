# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# There is a couple of ways this can be solved
# The main thing is we need a way to traverse backwards on a singly linked list, that's the whole thing
# We can reverse the original list and create a another list
# We can use hashtable to lookup parents and traverse backwards, in short, O(n) space info to traverse back
# Half the list we traverse forward, half we do backward

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        parent = {}
        current = head

        while current.next is not None:
            parent[current.next] = current
            current = current.next
        right = current
        left = head

        while True:
            if left is right:
                left.next = None
                break
            if parent[right] is left:
                right.next = None
                break
            _next = left.next
            left.next = right
            right.next = _next
            left = _next
            right = parent[right]
        return head


# followup, what if we reverse the half in place
# We don't need any table or another list for backward traversal
# This is a composite of three problems, find median pf a LL, reverse a LL and merger 2 LLs
# Bit tough for a ~30 minute interview