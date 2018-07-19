public class Solution
{
    public int numDistinct(String S, String T)
    {
        int[] dp = new int[T.length() + 1];

        for (int i = 1; i <= S.length(); i++)
        {
            dp[0] = 1;

            for (int j = T.length(); j >= 1; j--)
            {
                if (T.charAt(j - 1) == S.charAt(i - 1))
                {
                    dp[j] += dp[j - 1];
                }
            }
        }

        return dp[0];
    }
}
