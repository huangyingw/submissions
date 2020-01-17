public class Solution
{
    public int numDecodings(String s)
    {
        if (s == null || s.length() == 0)
        {
            return 0;
        }
        
        int[] dp = new int[s.length() + 1];
        dp[0] = 1;

        for (int i = 1; i < s.length(); i++)
        {
            if (s.charAt(i - 1) != '0')
            {
                dp[i] += dp[i - 1];
            }

            if (i -2 >= 0 && (s.charAt(i - 2) == '1' || (s.charAt(i - 2) == '2' && s.charAt(i - 1) <= '6')))
            {
                dp[i] += dp[i - 2];
            }
        }

        return dp[s.length()];
    }
}
