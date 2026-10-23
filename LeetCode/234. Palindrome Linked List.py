'''
This is a medium when constant Space constraint is enforced
O(n) space is no-brainer
O(1) space is where this is not ane easy problem anymore
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        nums = []
        while head is not None:
            nums.append(head.val)
            head = head.next
        return nums == nums[::-1]


# Find start of second part, and reverse it
# Then two pointer, head and tail, move forward and compare
# Just check the visual here, its exactly built from the solution
# Visual Here: https://claude.ai/share/37198054-4cc3-46f3-96e8-6e8888764b18 (half publicly available)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        slow = head
        fast = head
        while fast is not None:
            slow = slow.next
            fast = fast.next
            if fast is None:
                break
            fast = fast.next

        prev = None
        current = slow
        while current is not None:
            next_ = current.next
            current.next = prev
            prev = current
            current = next_

        right = prev
        left = head

        while right != None:
            if left.val != right.val:
                return False
            else:
                left = left.next
                right = right.next
        return True
# Time Complexity: O(n)
# Space Complexity: O(1) YaY