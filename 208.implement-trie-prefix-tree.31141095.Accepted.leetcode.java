class TrieNode
{
    char content;
    boolean isWord;
    Map<Character, TrieNode> nexts;
    public TrieNode()
    {
        this.content = ' ';
        this.isWord = false;
        this.nexts = new HashMap<Character, TrieNode>();
    }
    public TrieNode(char content)
    {
        this.content = content;
        this.isWord = false;
        this.nexts = new HashMap<Character, TrieNode>();
    }
}
public class Trie
{
    private TrieNode root;
    public Trie()
    {
        root = new TrieNode();
    }
    public void insert(String word)
    {
        if (search(word) == true)
        {
            return;
        }

        TrieNode current = root;

        for (int i = 0; i < word.length(); i++)
        {
            char c = word.charAt(i);
            TrieNode node = current.nexts.get(c);

            if (node == null)
            {
                current.nexts.put(c, new TrieNode(c));
                node = current.nexts.get(c);
            }

            current = node;
        }

        current.isWord = true;
    }
    public boolean search(String word)
    {
        TrieNode current = root;

        for (int i = 0; i < word.length(); i++)
        {
            TrieNode node = current.nexts.get(word.charAt(i));

            if (node == null)
            {
                return false;
            }

            current = node;
        }

        return current.isWord;
    }
    public boolean startsWith(String prefix)
    {
        TrieNode current = root;

        for (int i = 0; i < prefix.length(); i++)
        {
            TrieNode node = current.nexts.get(prefix.charAt(i));

            if (node == null)
            {
                return false;
            }

            current = node;
        }

        return true;
    }
}
