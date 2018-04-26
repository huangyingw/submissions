public class Solution
{
    public boolean wordBreak(String s, List<String> dict)
    {
        boolean[] dp = new boolean[s.length() + 1];
        dp[0] = true;

        for (int i = 0; i <= s.length(); i++)
        {
            if (dp[i])
            {
                for (int j = i + 1; j <= s.length(); j++)
                {
                    if (dict.contains(s.substring(i + 1, j)))
                    {
                        System.out.println("j --> " + j);
                        dp[j] = true;
                    }
                }
            }
        }

        return dp[s.length()];
    }
}
