
# Super short implementation using ordered dict
# More on python-recap
# You must know the internal implementation,
class LRUCache:

    def __init__(self, capacity: int):
        self.__dict = OrderedDict()
        self.__cap = capacity

    def get(self, key: int) -> int:
        if key not in self.__dict:
            return -1
        else:
            self.__dict.move_to_end(key, last=True)
            return self.__dict[key]

    def put(self, key: int, value: int) -> None:
        self.__dict[key] = value
        self.__dict.move_to_end(key, last=True)
        if len(self.__dict) > self.__cap:
            self.__dict.popitem(last=False)

# Time Complexity: Get: O(1) Put: O(1) __init__: O(1)
# Space complexity: linear



class Node:
    def __init__(self, val=None, pre=None, next_=None):
        self.val = val
        self.pre = pre
        self.next = next_



'''
Extremely messy implementation, lof of duplicate code
Doubly linked list + dict with sentinel head/tail

LRU cache class embeds a DLL logic, which makes it messy
A separate doubly linked list class will be more ideal
'''

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head
        self.cap = capacity
        self.dict = {}

    def get(self, key: int) -> int:
        if key in self.dict:
            current_node = self.dict[key][1]
            # new node at end
            new_node = Node(key, self.tail.pre, self.tail)
            self.tail.pre.next = new_node
            self.tail.pre = new_node
            # del the existing node
            current_node.pre.next = current_node.next
            current_node.next.pre = current_node.pre
            # new node reference on the dict
            val = self.dict[key][0]
            self.dict[key] = (val, new_node)
            return val
        else:
            return -1
    def put(self, key: int, value: int) -> None:
        if key not in self.dict:
            new_node = Node(key, self.tail.pre, self.tail)
            self.tail.pre.next = new_node
            self.tail.pre = new_node
            self.dict[key] = (value, new_node)
            # delete the front item, oldest
            if len(self.dict) > self.cap:
                key = self.head.next.val
                del self.dict[key]
                self.head.next.next.pre = self.head
                self.head.next = self.head.next.next

        else:
            # Refresh
            current_node = self.dict[key][1]
            # new node at end
            new_node = Node(key, self.tail.pre, self.tail)
            self.tail.pre.next = new_node
            self.tail.pre = new_node
            # del the existing node
            current_node.pre.next = current_node.next
            current_node.next.pre = current_node.pre
            self.dict[key] = (value, new_node)
'''
Cleanest solution and also largest and most time consuming
Node Class -> Doubly Linked List (DLL) and Then LRU class: Gradual buildup
Instead of discussing this, try to discuss the implementation with interviewer, thats better
'''

class Node:
    def __init__(self, val=None, pre=None, next_=None):
        self.val = val
        self.pre = pre
        self.next = next_


class DoublyList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head

    def append(self, key) -> Node:
        node = Node(key, self.tail.pre, self.tail)
        self.tail.pre.next = node
        self.tail.pre = node
        return node

    def delete(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        del node

    def get_front(self):
        return self.head.next


class LRUCache:

    def __init__(self, capacity: int):
        self.dll = DoublyList()
        self.cap = capacity
        self.dict = {}

    def get(self, key: int) -> int:
        if key in self.dict:
            val, node = self.dict[key]
            self.dll.delete(node)
            new_node = self.dll.append(key)
            self.dict[key] = (val, new_node)
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            val, current_node = self.dict[key]
            self.dll.delete(current_node)
            new_node = self.dll.append(key)
            self.dict[key] = (value, new_node)
        else:
            new_node = self.dll.append(key)
            self.dict[key] = (value, new_node)
            if len(self.dict) > self.cap:
                front = self.dll.get_front()
                del self.dict[front.val]
                self.dll.delete(front)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
