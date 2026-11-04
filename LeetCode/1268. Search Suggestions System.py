'''
Trie Based Solution
Bombed AWS PS because i forgot Trie Implementation, came up with Trie Code Very last Moment but there was no
time to code BFS part


'''
class Solution:
    def suggestedProducts(
            self, products: list[str], searchWord: str) -> list[list[str]]:

        root = {}
        for word in products:
            current = root
            for char in word:
                if char in current:
                    current = current[char]
                else:
                    current[char] = {}
                    current = current[char]
            current[None] = None

        def findMatches(s: str) -> list[str]:
            res = []
            current = root
            for char in s:
                if char in current:
                    current = current[char]
                else:
                    return []
            que = deque([(current, list(s))])
            while que:
                node, state = que.popleft()
                if node is None:
                    res.append("".join(state))
                    continue
                for nxt in node:
                    new_state = state[:]
                    if nxt is not None:
                        new_state.append(nxt)
                    que.append((node[nxt], new_state))

            res.sort()
            return res[0:3]

        output = []
        current = ""
        for s in searchWord:
            current = current + s
            output.append(findMatches(current))
        return output

# Let m = number of products, n = length of the longest product,
# L = length of searchWord.
#
# Trie build: O(m*n), inserting m words of up to n characters each.
#
# Queries: findMatches is called L times, once per prefix. Each call:
#   - Walks down to the prefix node: O(L), absorbed by the terms below.
#   - BFS: the subtree can contain up to m*n nodes, and copying the
#     state at each node costs up to O(n), so O(m*n*n).
#   - Sort: O(m log m) comparisons, each comparing up to n characters,
#     so O(n * m log m).
#
# Total: O(m*n + L * (m*n*n + n * m log m))
#      = O(L * m * n * (n + log m))

# Space Complexity:
#
# Trie: O(m*n), up to m*n nodes for m words of up to n characters.
#
# BFS queue (per call): each trie level has at most m nodes, since every
#   node at a given depth is a prefix of at least one distinct word. The
#   queue holds at most two levels at once, so O(m) entries, each with a
#   state of up to n characters: O(m*n).
#
# res (per call): up to m matched words of up to n characters: O(m*n).
#   Only one call is active at a time, so this space is reused.
#
# Output: L lists of up to 3 words of up to n characters: O(L*n).
#
# Total: O(m*n + L*n)