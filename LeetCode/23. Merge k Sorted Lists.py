# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merged_list = ListNode()
        head = merged_list
        while True:
            min_idx = -1
            min_val = math.inf
            for idx, lst in enumerate(lists):
                if lst is not None and lst.val < min_val:
                    min_idx = idx
                    min_val = lst.val
            if min_idx == -1:
                break
            merged_list.next = lists[min_idx]
            merged_list = merged_list.next
            lists[min_idx] = lists[min_idx].next
            merged_list.next = None

        return head.next
    # Time Complexity: O(n*k), n = total sum of nodes, K = no of lists. On each iteration we insert one node, and we loop through K lists
    # Space Complexity: O(1) we reusing existing nodes


# This is a better approach
# Using a Heap to get the min node
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        head = ListNode()
        merged = head
        heap = []
        cnt = count()
        for lst in lists:
            if lst is not None:
                heap.append((lst.val, next(cnt), lst))
        heapq.heapify(heap) # O(k)
        while heap: # logK each time, total all nodes means n times
            _, _, node = heapq.heappop(heap)
            merged.next = node
            merged = merged.next
            if node.next is not None:
                heapq.heappush(heap, (node.next.val, next(cnt), node.next))
        return head.next
    # Time Complexity: O(n log K + n) -> O(nlogK)
    # SPace: O(k) for K item heap
