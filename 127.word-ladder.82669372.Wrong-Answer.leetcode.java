public class Solution
{
    public int ladderLength(String start, String end, Set<String> dict)
    {
        if (dict.size() == 0)
        {
            return 0;
        }

        LinkedList<String> wordQueue = new LinkedList<String>();
        wordQueue.add(start);
        int currDistance = 1;

        while (!wordQueue.isEmpty())
        {
            String currWord = wordQueue.pop();

            if (currWord.equals(end))
            {
                return currDistance;
            }

            for (int i = 0; i < currWord.length(); i++)
            {
                char[] currCharArr = currWord.toCharArray();

                for (char c = 'a'; c <= 'z'; c++)
                {
                    currCharArr[i] = c;
                    String newWord = new String(currCharArr);

                    if (dict.contains(newWord))
                    {
                        wordQueue.add(newWord);
                        currDistance++;
                        dict.remove(newWord);
                    }
                }
            }
        }

        return 0;
    }
}
