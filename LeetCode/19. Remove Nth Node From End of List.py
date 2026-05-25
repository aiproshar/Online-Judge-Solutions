# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Easy solution, find len, and then find the node to remove
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current_node = head
        len_ = 0

        while current_node is not None:
            len_ += 1
            current_node = current_node.next
        len_ = len_ - n
        if len_ == 0:
            head = head.next
            return head

        current_node = head

        # We don't want to end up on the node to remove, we want the previous parent
        # That's why -2
        while len_ - 1 > 0:
            current_node = current_node.next
            len_ -= 1

        current_node.next = current_node.next.next
        return head

# Followup -> can we do it in one pass ? AKA do it without knowing the length

# Use dummy node to support more fined loop invariant
# Also we want to reach the last node, node the null, because alrready +1 offset by dummy head

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        current_node = dummy
        delete_node = dummy

        while n > 0:
            current_node = current_node.next
            n -= 1

        while current_node.next is not None:
            current_node = current_node.next
            delete_node = delete_node.next
        delete_node.next = delete_node.next.next
        return dummy.next
# Time and space complexity: Same as previous