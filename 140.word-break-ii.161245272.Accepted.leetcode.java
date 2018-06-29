public class Solution
{
    public List<String> wordBreak(String s, List<String> dict)
    {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        Map<String, ArrayList<String>> map = new HashMap<String, ArrayList<String>>();
        return wordBreakHelper(s, dict, map);
    }

    public List<String> wordBreakHelper(String s, List<String> dict, Map<String, ArrayList<String>> memo)
    {
        if (memo.containsKey(s))
        {
            return memo.get(s);
        }

        ArrayList<String> result = new ArrayList<String>();
        int n = s.length();

        if (n <= 0)
        {
            return result;
        }

        for (int len = 1; len <= n; ++len)
        {
            String subfix = s.substring(0, len);

            if (dict.contains(subfix))
            {
                if (len == n)
                {
                    result.add(subfix);
                }
                else
                {
                    String prefix = s.substring(len);
                    List<String> tmp = wordBreakHelper(prefix, dict, memo);

                    for (String item : tmp)
                    {
                        item = subfix + " " + item;
                        result.add(item);
                    }
                }
            }
        }

        memo.put(s, result);
        return result;
    }
}

