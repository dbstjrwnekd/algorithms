class TrieNode:
    def __init__(self, word=None):
        self.word = word
        self.children = {}
        self.end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        step = self.root
        for c in word:
            if c not in step.children:
                step.children[c] = TrieNode(c)
            step = step.children[c]
        step.end = True

    def search(self, word: str) -> bool:
        step = self.root
        for c in word:
            if c not in step.children:
                return False
            step = step.children[c]
        return step.end
        

    def startsWith(self, prefix: str) -> bool:
        step = self.root
        for c in prefix:
            if c not in step.children:
                return False
            step = step.children[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)