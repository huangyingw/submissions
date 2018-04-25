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
                    System.out.println("s.substring(i, j) --> " + s.substring(i, j));

                    if (dict.contains(s.substring(i, j)))
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
