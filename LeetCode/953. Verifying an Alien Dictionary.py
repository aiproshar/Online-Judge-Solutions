class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        val = dict()

        for i in range(len(order)):
            val[order[i]] = i

        for k in range(1, len(words)):
            first = words[k - 1]
            second = words[k]

            i = 0
            # out of length / out of bound
            ool = True
            while i < len(first) and i < len(second):

                if val[first[i]] > val[second[i]]:
                    return False
                elif val[first[i]] < val[second[i]]:
                    ool = False
                    break
                else:
                    i += 1
            # We terminated the loop due to out of bound
            # So now all chars matched till term, the sorter word must come first
            if ool:
                if len(first) > len(second):
                    return False

        return True

# Simple Greedy Type Algo
# Don't know where graph is taking apart here
# Time Complexity: 