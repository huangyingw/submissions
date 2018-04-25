public class Solution
{
    public boolean isInterleave(String s1, String s2, String s3)
    {
        if (s1.length() + s2.length() != s3.length())
        {
            return false;
        }

        boolean[] dp = new boolean[s2.length() + 1];

        for (int i = 0; i <= s1.length(); i++)
        {
            for (int j = s2.length(); j >= 0; j--)
            {
                dp[j] = (i == 0 && j == 0)
                        || (i != 0 && dp[j] && s1.charAt(i - 1) == s3.charAt(i + j - 1))
                        || (j != 0 && dp[j - 1] && s2.charAt(j - 1) == s3.charAt(i + j
                                - 1));
            }
        }

        return dp[s2.length()];
    }
}

