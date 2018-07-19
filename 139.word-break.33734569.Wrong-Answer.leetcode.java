public class Solution
{
    public boolean wordBreak(String s, Set<String> dict)
    {
        assert!s.isEmpty();
        boolean[] dp = new boolean[s.length() + 1];
        dp[0] = true;

        for (int start = 0; start < s.length(); start++)
        {
            for (int end = start + 1; end <= s.length(); end++)
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
