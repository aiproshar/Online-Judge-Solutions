class FileNode:
    def __init__(self, is_file=False):
        if is_file:
            self.children = None
            self.content = ""  # append only string
        else:
            self.children = {}
            self.content = None  # append operation will fail, deliberate choice
        self.is_file = is_file


class FileSystem:

    def __init__(self):

        self.root = FileNode()

    def ls(self, path: str) -> List[str]:

        current = self.root
        if path == "/":
            return sorted(list(current.children.keys()))

        path = path[1:].split('/')

        for dir_ in path:
            if dir_ not in current.children:
                return []
            current = current.children[dir_]

        if current.is_file:
            return [path[-1]]
        else:
            return sorted(list(current.children.keys()))

    def mkdir(self, path: str) -> None:

        current = self.root
        path = path[1:].split('/')

        for dir_ in path:
            if dir_ not in current.children:
                current.children[dir_] = FileNode()
            current = current.children[dir_]

    def addContentToFile(self, filePath: str, content: str) -> None:
        current = self.root
        path = filePath[1:].split('/')

        for dir_ in path[:-1]:
            if dir_ not in current.children:
                current.children[dir_] = FileNode()
            current = current.children[dir_]
        # final node
        if path[-1] in current.children:
            current = current.children[path[-1]]
            current.content += content
        else:
            current.children[path[-1]] = FileNode(True)
            current = current.children[path[-1]]
            current.content = content

    def readContentFromFile(self, filePath: str) -> str:
        current = self.root
        path = filePath[1:].split('/')

        for dir_ in path[:-1]:
            if dir_ not in current.children:
                return ""
            current = current.children[dir_]

        if path[-1] not in current.children:
            return ""
        current = current.children[path[-1]]
        if current.is_file:
            return current.content
        else:
            return ""

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)