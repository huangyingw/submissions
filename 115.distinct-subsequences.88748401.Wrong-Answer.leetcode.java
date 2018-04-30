public class Solution
{
    public int numDistinct(String S, String T)
    {
        int[] dp = new int[T.length() + 1];
        dp[0] = 1;

        for (int i = 1; i <= S.length(); i++)
        {
            for (int j = 1; j <= T.length(); j++)
            {
                if (T.charAt(j - 1) == S.charAt(i - 1))
                {
                    dp[j] += dp[j - 1];
                    System.out.println(j + " --> " + dp[j]);
                }
            }

            System.out.println();
        }

        return dp[T.length()];
    }
}
