public class Solution
{
    class WordNode
    {
        String word;
        int steps;

        public WordNode(String word, int steps)
        {
            this.word = word;
            this.steps = steps;
        }
    }
    public int ladderLength(String beginWord, String endWord, List<String> wordDict)
    {
        Queue<WordNode> queue = new LinkedList<WordNode>();
        queue.add(new WordNode(beginWord, 1));
        wordDict.add(endWord);

        while (!queue.isEmpty())
        {
            WordNode top = queue.poll();
            String word = top.word;

            if (word.equals(endWord))
            {
                return top.steps;
            }

            char[] arr = word.toCharArray();

            for (int i = 0; i < arr.length; i++)
            {
                char temp = arr[i];

                for (char c = 'a'; c <= 'z'; c++)
                {
                    arr[i] = c;
                    String newWord = new String(arr);

                    if (wordDict.contains(newWord))
                    {
                        queue.offer(new WordNode(newWord, top.steps + 1));
                        wordDict.remove(newWord);
                    }
                }

                arr[i] = temp;
            }
        }

        return 0;
    }
}
