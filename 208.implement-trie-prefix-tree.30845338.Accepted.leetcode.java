class TrieNode
{
    char content;
    boolean isEnd;
    LinkedList<TrieNode> childNode;
    public TrieNode()
    {
        this.content = ' ';
        this.isEnd = false;
        this.childNode = new LinkedList<TrieNode>();
    }
    public TrieNode(char content)
    {
        this.content = content;
        this.isEnd = false;
        this.childNode = new LinkedList<TrieNode>();
    }
    public TrieNode subNode(char content)
    {
        if (childNode != null)
        {
            for (TrieNode node : childNode)
            {
                if (node.content == content)
                {
                    return node;
                }
            }
        }

        return null;
    }
}
public class Trie
{
    private TrieNode root;
    public Trie()
    {
        root = new TrieNode();
    }
    // Inserts a word into the trie.
    public void insert(String word)
    {
        if (search(word) == true)
        {
            return;
        }

        TrieNode current = root;

        for (int i = 0; i < word.length(); i++)
        {
            TrieNode node = current.subNode(word.charAt(i));

            if (node == null)
            {
                current.childNode.add(new TrieNode(word.charAt(i)));
                node = current.subNode(word.charAt(i));
            }

            current = node;
        }

        current.isEnd = true;
    }
    // Returns if the word is in the trie.
    public boolean search(String word)
    {
        TrieNode current = root;

        for (int i = 0; i < word.length(); i++)
        {
            TrieNode node = current.subNode(word.charAt(i));

            if (node == null)
            {
                return false;
            }

            current = node;
        }

        if (current.isEnd == false)
        {
            return false;
        }
        else
        {
            return true;
        }
    }
    // Returns if there is any word in the trie
    // that starts with the given prefix.
    public boolean startsWith(String prefix)
    {
        TrieNode current = root;

        for (int i = 0; i < prefix.length(); i++)
        {
            TrieNode node = current.subNode(prefix.charAt(i));

            if (node == null)
            {
                return false;
            }

            current = node;
        }

        return true;
    }
}
// Your Trie object will be instantiated and called as such:
// Trie trie = new Trie();
// trie.insert("somestring");
// trie.search("key");
