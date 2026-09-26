
class Solution:

    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0:
            return s
        temp = Counter(s)
        # max heap, first item frequency, second char
        heap = []
        for char, count in temp.items():
            heapq.heappush(heap, (-count, char))

        # slice length

        current = []
        # EOL marker, we're considering the last run, where we can have any items
        EOL = False
        while heap:
            temp = []
            for _ in range(k):
                if not heap:
                    if EOL:
                        # Invalid state
                        return ""
                    else:
                        EOL = True
                        break
                count, char = heapq.heappop(heap)
                current.append(char)
                temp.append([count, char])

            while temp:
                count, char = temp.pop()
                count += 1
                if count < 0:
                    heapq.heappush(heap, (count, char))

        return "".join(current)

# Time Complexity: O(n) + nlogK where k is 26 so n.C ~ O(n)
# Space: O(n)