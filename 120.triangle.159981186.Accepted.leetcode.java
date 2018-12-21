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

        for (int row = rows - 2; row >= 0; row--)
        {
            for (int j = 0; j <= row; j++)
            {
                dp[j] = Math.min(dp[j], dp[j + 1]) + triangle.get(row).get(j);
            }
        }

        return dp[0];
    }
}
