public class Solution
{
    public boolean wordBreak(String s, Set<String> dict)
    {
        assert!s.isEmpty();
        boolean[] dp = new boolean[s.length() + 1];
        dp[0] = true;

        for (int end = 1; end <= s.length(); end++)
        {
            for (int start = 0; start < end; start++)
            {
                if (dp[start] && dict.contains(s.substring(start, end)))
                {
                    dp[end] = true;
                    break;
                }
            }
        }

        return dp[s.length()];
    }
}
