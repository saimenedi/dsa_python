class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isLeaf = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert (self, key):
        curr = self.root
        for c in key:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.isLeaf = True

    def search(self, key):
        curr = self.root
        for c in key:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return curr.isLeaf

    def isPrefix(self, prefix):
        curr = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return True


if __name__ == "__main__":
    trie = Trie()
    arr = ["and", "ant", "do", "dad"]
    for s in arr:
        trie.search(s)
    searchKeys = ["do", "gee", "bat"]
    for s in searchKeys:
        if trie.search(s):
            print("true", end=" ")
        else:
            print("false", end=" ")

    print()
    prefixKeys = ["ge", "ba", "do", "de"]
    for s in prefixKeys:
        if trie.isPrefix:
            print("true", end=" ")
        else:
            print("false", end=" ")
    print()