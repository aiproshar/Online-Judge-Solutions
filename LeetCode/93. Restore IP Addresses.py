class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        res = []

        def backtrack(idx, current):
            if idx == n and len(current) == 4:
                res.append(".".join(current))
            # Early termination on both conditions
            # 1.2.3.22.1212 -> to much split already, ging forward no help
            #-----------i is here
            # 22.22.222
            #           i is here, we reached end but not 4 splits
            if idx == n or len(current) > 4:
                return

            for i in range(idx, n):

                temp = s[idx:i + 1]
                if len(temp) > 1 and temp[0] == '0':
                    break
                if int(temp) > 255:
                    break
                current.append(temp)
                backtrack(i + 1, current)
                current.pop()
            return

        backtrack(0, [])
        return res


# Time Complexity: We can take one/two/three element and go to next, so 3 choices
# Ho far we go ? ideally 4 elements depth, because we do early termination
# So Time Complexity: 3^4 -> O(1)
# Space: The split IP address, since its called at 12 len, we can trat this as O(1)



