# default implementation
# Time complexity: O(n)
# Space complexity: O(1) -> no of uniq elements
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_count = Counter(s)
        t_count = Counter(t)

        for key in s_count:
            if s_count[key] != t_count.get(key, 0):
                return False
        return True



# Array-based frequency counting with a single fixed-size list.
# In C++/Go/Rust, this would be a contiguous stack-allocated array
# that fits in 1-2 L1 cache lines — extremely fast.
# In Python, the list stores pointers to heap-allocated PyInt objects,
# so we lose cache locality. The real bottleneck is boxing/unboxing
# overhead on every access, not memory layout.
# Still faster than Counter/dict due to avoiding hash overhead.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        word_freq = [0 for _ in range(0, 26)]

        for char in s:
            word_freq[ord(char) - ord('a')] += 1
        for char in t:
            word_freq[ord(char) - ord('a')] -= 1
        for freq in word_freq:
            if freq != 0:
                return False
        return True

