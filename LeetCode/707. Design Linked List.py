# initially thought of having tail pointer and size variable, but that also introduced a bit complexity
# If interviewer wants constant time add at tail, then we should store tail index, and also size for easing up some operations
# TLDR: singly linked list with head pointer
class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = None
    def get(self, index: int) -> int:
        current = self.head
        while index > 0:
            if current is None:
                return -1
            current = current.next
            index -= 1
        if current is None:
            return -1
        return current.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val, self.head)
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        if self.head is None:
            self.addAtHead(val)
            return
        current = self.head
        while current.next is not None:
            current = current.next
        new_node = Node(val)
        current.next = new_node
    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        current = self.head
        while index - 1 > 0:
            if current is None:
                return
            current = current.next
            index -= 1
        if current is None:
            return
        new_node = Node(val, current.next)
        current.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            if self.head is None:
                return
            self.head = self.head.next
            return
        current = self.head
        while index - 1 > 0:
            if current is None:
                return
            current = current.next
            index -= 1
        if current is None or current.next is None:
            return
        current.next = current.next.next



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)