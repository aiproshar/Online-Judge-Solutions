class RandomizedSet:

    def __init__(self):
        # List containing all the values
        self.lst = []
        # value -> index in list mapping
        self.vals = {}

    def insert(self, val: int) -> bool:
        if val in self.vals:
            return False
        self.lst.append(val)
        # inserted at the last
        self.vals[val] = len(self.lst) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.vals:
            return False
        # swap with the last item and pop
        val_idx = self.vals[val]
        last_item = self.lst[-1]
        self.vals[last_item] = val_idx
        self.lst[val_idx] = last_item
        del self.vals[val]
        self.lst.pop()
        return True

    def getRandom(self) -> int:
        rand_idx = random.randint(0, len(self.lst) - 1)
        return self.lst[rand_idx]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()