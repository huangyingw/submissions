public class Solution
{
    public int minimumTotal(List<List<Integer>> triangle)
    {
        int rows = triangle.size();
        int[] dp = new int[rows];

        for (int j = 0; j < rows; j++)
        {
            dp[j] = triangle.get(rows - 1).get(j);
        }

        for (int i = rows - 2; i >= 0; i--)
        {
            for (int j = 0; j < i; j++)
            {
                dp[j] = Math.min(dp[j], dp[j + 1]) + triangle.get(i).get(j);
            }
        }

        return dp[0];
    }
}
