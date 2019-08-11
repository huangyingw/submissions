public class Solution
{
    public int minimumTotal(List<List<Integer>> triangle)
    {
        int rows = triangle.size();
        int[] dp = new int[rows + 1];
        Arrays.fill(dp, 0);

        for (int row = rows - 1; row >= 0; row--)
        {
            for (int col = 0; col <= row; col++)
            {
                dp[col] = triangle.get(row).get(col) + Math.min(dp[col], dp[col + 1]);
            }
        }

        return dp[0];
    }
}
