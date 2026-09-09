

# Advanced BFS problem
# There is no child info/Adj List/ Adj Matrix
# We calculate the child nodes on the fly. Also depth map for tracking which childs was visited on the fly

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        wordList = set(wordList)
        if endWord not in wordList:
            return 0

        depth = {beginWord: 1}
        que = deque([beginWord])
        while que:
            current = que.popleft()
            for i in range(len(current)):
                current_list = list(current)
                for char in string.ascii_lowercase:
                    current_list[i] = char
                    child = "".join(current_list)
                    if child not in wordList or child in depth:
                        continue
                    depth[child] = depth[current] + 1
                    if child == endWord:
                        # early termination
                        return depth[child]
                    que.append(child)
        return 0

# Time Complexity: We visit N nodes, for each nodes, we generate L*26 words  (Double for loop), so it should be L*26*M ? No, you are mistaken
# Line: 25 -> child_str = "".join(child) -> This is another linear operation in the for loop, So in L*26*M there is another L
# So time complexity: L^2*M (removing constant 26)
# Space complexity: All nodes in the queue, so L*M