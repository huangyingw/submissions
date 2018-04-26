public class Solution
{
    public int minimumTotal(List<List<Integer>> triangle)
    {
        int len = triangle.get(triangle.size() - 1).size();
        int[] dp = new int[len];

        for (int i = 0; i < len; i++)
        {
            dp[i] = triangle.get(triangle.size() - 1).get(i);
        }

        for (int row = triangle.size() - 2; row >= 0; row--)
        {
            for (int i = 0; i <= row; i++)
            {
                dp[i] = triangle.get(row).get(i) + Math.min(dp[i], dp[i + 1]);
            }
        }

        return dp[0];
    }
}
