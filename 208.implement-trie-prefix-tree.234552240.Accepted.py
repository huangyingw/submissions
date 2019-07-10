"""
Implement a trie with insert, search, and startsWith methods.
Example:
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
Note:
You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.

        Initialize your data structure here.

        Inserts a word into the trie.
        :type word: str
        :rtype: void

        Returns if the word is in the trie.
        :type word: str
        :rtype: bool

        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.dic
        for c in prefix:
            if c in cur:
                cur = cur[c]
            else:
                return False
        return True
