public class Solution
{
    public boolean wordBreak(String s, Set<String> dict)
    {
        assert!s.isEmpty();
        boolean[] dp = new boolean[s.length() + 1];
        dp[0] = true;

        for (int start = 0; start < s.length(); start++)
        {
            if (!dp[start])
            {
                continue;
            }

            for (int end = start + 1; end <= s.length(); end++)
            {
                if (dict.contains(s.substring(start, end)))
                {
                    dp[end] = true;
                }
            }
        }

        return dp[s.length()];
    }
}

