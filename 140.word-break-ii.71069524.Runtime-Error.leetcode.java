<<< <<< < Updated upstream
public class Solution
{
    public List<String> wordBreak(String s, Set<String> dict)
    {
        @SuppressWarnings("unchecked") List<String> dp[] =
            new ArrayList[s.length() + 1];
        dp[0] = new ArrayList<String>();

        for (int start = 0; start < s.length(); start++)
        {
            for (int end = s.length(); end > start; end--)
            {
                String word = s.substring(start, end);

                if (dict.contains(word))
                {
                    if (dp[end] == null)
                    {
                        dp[end] = new ArrayList<String>();
                    }

                    dp[end].add(word);
                }
            }
        }

        List<String> result = new LinkedList<String>();

        if (dp[s.length()] == null)
        {
            return result;
        }

        ArrayList<String> current = new ArrayList<String>();
        dfs(dp, s.length(), result, current);
        return result;
        == == == =
            public class Solution
        {
            public List<String> wordBreak(String s, Set<String> dict)
            {
                @SuppressWarnings("unchecked") List<String> dp[] =
                    new ArrayList[s.length() + 1];
                dp[0] = new ArrayList<String>();

                for (int start = 0; start < s.length(); start++)
                {
                    for (int end = s.length(); end > start; end--)
                    {
                        String word = s.substring(start, end);

                        if (dict.contains(word))
                        {
                            if (dp[end] == null)
                            {
                                dp[end] = new ArrayList<String>();
                            }

                            dp[end].add(word);
                        }
                    }
                }

                List<String> result = new LinkedList<String>();

                if (dp[s.length()] == null)
                {
                    return result;
                }

                ArrayList<String> current = new ArrayList<String>();
                dfs(dp, s.length(), result, current);
                return result;
                >>> >>> > Stashed changes
            }

            public void dfs(List<String> dp[], int end, List<String> result,
                            ArrayList<String> current)
            {
                <<< <<< < Updated upstream

                if (end <= 0)
                {
                    String ans = current.get(current.size() - 1);

                    for (int i = current.size() - 2; i >= 0; i--)
                    {
                        ans += (" " + current.get(i));
                    }

                    result.add(ans);
                    return;
                }

                for (String str : dp[end])
                {
                    current.add(str);
                    dfs(dp, end - str.length(), result, current);
                    current.remove(current.size() - 1);
                }
            }
        }
        == == == =

            if (end <= 0)
        {
            String ans = current.get(current.size() - 1);

            for (int i = current.size() - 2; i >= 0; i--)
            {
                ans += (" " + current.get(i));
            }

            result.add(ans);
            return;
        }

        for (String str : dp[end])
        {
            current.add(str);
            dfs(dp, end - str.length(), result, current);
            current.remove(current.size() - 1);
        }
    }
}
>>> >>> > Stashed changes
