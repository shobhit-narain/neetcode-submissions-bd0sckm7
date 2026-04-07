class Node:

    def __init__(self) -> None:
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.end = True

    def search(self, word: str) -> bool:
        def dfs(pos, root):
            curr = root
            for idx in range(pos, len(word)):
                if word[idx] == ".":
                    for ch in curr.children.values():
                        if dfs(idx + 1, ch):
                            return True
                    return False
                if word[idx] not in curr.children:
                    return False
                curr = curr.children[word[idx]]
            return curr.end

        return dfs(0, self.root)
