# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next




'''
Stack to reverse portion of linkedlist
Edge case if last group is smaller than K then must not be reversed

'''
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        sen = ListNode()
        sen.next = head
        head = sen

        pre = head
        current = head.next
        next = None

        while current is not None:
            lst = []
            while len(lst) < k and current is not None:
                lst.append(current)
                current = current.next
                # This next line is must or last K group will create a circle
                lst[-1].next = None
            # As per problem statement, if last group is smaller than K we don't reverse
            if len(lst) < k:
                lst.reverse()
            while lst:
                pre.next = lst.pop()
                pre = pre.next
        return head.next
# Time Complexity: O(n) -> We process n nodes, each once
# Space complexity: O(k) -> At most K node ref in the list
