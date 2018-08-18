class WordTrieNode
{
    boolean isWord;
    int index;
    HashMap<Character, WordTrieNode> nexts;

    public WordTrieNode()
    {
        nexts = new HashMap<Character, WordTrieNode>();
    }
}

public class WordDictionary
{
    private WordTrieNode root;

    public WordDictionary()
    {
        root = new WordTrieNode();
    }

    public void addWord(String word)
    {
        WordTrieNode p = root;
        int i = 0, len = word.length();

        while (i < len)
        {
            char ch = word.charAt(i);

            if (p.nexts.containsKey(ch))
            {
                p = p.nexts.get(ch);
                i ++;
            }
            else
            {
                break;
            }
        }

        while (i < len)
        {
            WordTrieNode newNode = new WordTrieNode();
            newNode.index = i;
            p.nexts.put(word.charAt(i), newNode);
            p = newNode;
            i ++;
        }

        p.isWord = true;
    }

    public boolean search(String word)
    {
        if (word == null || word.length() == 0)
        {
            return false;
        }

        WordTrieNode p = root;
        return dfs(word, 0, p);
    }

    private boolean dfs(String word, int index, WordTrieNode p)
    {
        if (index == word.length() - 1)
        {
            if (word.charAt(index) == '.')
            {
                for (WordTrieNode node : p.nexts.values())
                {
                    if (node.isWord)
                    {
                        return true;
                    }
                }

                return false;
            }
            else
            {
                WordTrieNode endNode = p.nexts.get(word.charAt(index));
                return endNode != null && endNode.isWord;
            }
        }

        if (index >= word.length())
        {
            return false;
        }

        if (word.charAt(index) == '.')
        {
            boolean result = false;

            for (WordTrieNode node : p.nexts.values())
            {
                result |= dfs(word, index + 1, node);
            }

            return result;
        }
        else
        {
            if (p.nexts.containsKey(word.charAt(index)))
            {
                return dfs(word, index + 1, p.nexts.get(word.charAt(index)));
            }
            else
            {
                return false;
            }
        }
    }
}
