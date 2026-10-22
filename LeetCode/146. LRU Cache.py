
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


'''
Extremely messy implementation, lof of duplicate code
Doubly linked list + dict with sentinel head/tail

LRU cache class embeds a DLL logic, which makes it messy
A separate doubly linked list class will be more ideal
'''


class Node:
    def __init__(self, key, prev=None, next=None):
        self.prev = prev
        self.next = next
        self.key = key


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.len = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.data = {}

    def get(self, key: int) -> int:
        if key in self.data:
            # deletion
            node = self.data[key][1]
            node.prev.next = node.next
            node.next.prev = node.prev
            del node
            # Append at end
            value = self.data[key][0]
            node = Node(key)
            node.next = self.tail
            node.prev = self.tail.prev
            node.prev.next = node
            node.next.prev = node
            # update the HashTable
            self.data[key] = (value, node)
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            # deletion
            node = self.data[key][1]
            node.prev.next = node.next
            node.next.prev = node.prev
            # Append at end
            node = Node(key)
            node.next = self.tail
            node.prev = self.tail.prev
            node.prev.next = node
            node.next.prev = node
            # update the HashTable
            self.data[key] = (value, node)
        else:
            # append at end
            node = Node(key)
            node.next = self.tail
            node.prev = self.tail.prev
            node.prev.next = node
            node.next.prev = node
            # update the HashTable
            self.data[key] = (value, node)

            self.len += 1
            # Evict LRU
            if self.len > self.capacity:
                node = self.head.next
                node.prev.next = node.next
                node.next.prev = node.prev
                del self.data[node.key]
                self.len -= 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


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




'''
Modular and cleaner Solution, this one mimics ordered dict
Instead of shoving all the linked list logic in the main methods, we implement helper methods
Helper methods interface is very similar to ordered dict
Key as identifier everywhere, not node
'''


class Node:
    def __init__(self, key=None, prev=None, next=None):
        self.key = key  # do find and delete hashmap entry
        self.prev = prev
        self.next = next


class LRUCache:

    def move_to_end(self, key) -> None:

        node = self.data[key][1]
        # update old neighbours
        node.prev.next = node.next
        node.next.prev = node.prev

        # upate node pointers
        node.prev = self.tail.prev
        node.next = self.tail
        # update new neighbours
        self.tail.prev.next = node
        self.tail.prev = node

    def popfirst(self):
        node = self.head.next
        key = node.key

        self.head.next = node.next
        node.next.prev = self.head

        # cleanup
        del self.data[key]
        del node

    def append_to_end(self, key) -> Node:

        node = Node(key=key)
        node.prev = self.tail.prev
        node.next = self.tail

        # update new neighbours
        self.tail.prev.next = node
        self.tail.prev = node
        return node

    def __init__(self, capacity: int) -> None:

        self.head = Node()
        self.tail = Node()
        # key -> (value, Node)
        self.data = {}
        self.cap = capacity

        #
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1

        self.move_to_end(key)
        return self.data[key][0]

    def put(self, key: int, value: int) -> None:

        if key not in self.data:

            node = self.append_to_end(key)
            self.data[key] = (value, node)
            if len(self.data) > self.cap:
                self.popfirst()
        else:
            _, node = self.data[key]
            self.data[key] = (value, node)
            self.move_to_end(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
