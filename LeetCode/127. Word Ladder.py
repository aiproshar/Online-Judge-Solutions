

# Advanced BFS problem
# There is no child info/Adj List/ Adj Matrix
# We calculate the child nodes on the fly. Also depth map for tracking which childs was visited on the fly

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        depth = collections.defaultdict(lambda: -1)

        wordList = set(wordList)


        que = collections.deque()

        que.append(beginWord)
        depth[beginWord] = 1
        while que:
            current = que.popleft()
            for i in range(len(current)):
                child = list(current)
                for j in string.ascii_lowercase:
                    child[i] = j
                    child_str = "".join(child)
                    if child_str in wordList and depth[child_str] == -1:
                        depth[child_str] = depth[current] + 1
                        if child_str == endWord:
                            return depth[child_str]
                        que.append(child_str)

        return 0
