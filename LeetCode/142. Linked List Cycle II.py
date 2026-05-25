# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Basic easy Hashtable (set) lookup
# Put each node in set, check if twe encountered them before
# Also None check for safety
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None

        visited = set()

        current_node = head

        while current_node is not None:
            if current_node in visited:
                return current_node
            else:
                visited.add(current_node)
                current_node = current_node.next
        return None

# Time complexity: O(n)
# Space complexity: O(n)


# Extended floyd's cycle detection algorithm
# Some math behind it on the internet
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        slow = head.next
        fast = head.next.next

        while slow is not fast:
            slow = slow.next
            if fast is None or fast.next is None:
                return None
            fast = fast.next
            fast = fast.next
        another_node = head
        while another_node is not slow:
            another_node = another_node.next
            slow = slow.next
        return slow

# time complexity: O(n)
# Space complexity: O(1)