public class Solution
{
    public int minPathSum(int[][] grid)
    {
        assert grid != null && grid.length != 0 && grid[0].length != 0;
        int[] dp = new int[grid[0].length];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;

        for (int i = 0; i < grid.length; i++)
        {
            for (int j = 0; j < grid[0].length - 1; j++)
            {
                dp[j + 1] = Math.min(dp[j + 1], dp[j]) + grid[i][j + 1];
            }
        }

        return dp[grid[0].length - 1];
    }
}

