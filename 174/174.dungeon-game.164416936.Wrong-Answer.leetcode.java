public class Solution
{
    public int calculateMinimumHP(int[][] dungeon)
    {
        int m = dungeon.length, n = dungeon[0].length;
        int[] dp = new int[n + 1];
        Arrays.fill(dp, 1);

        for (int i = m - 1; i >= 0; i--)
        {
            dp[n - 1] -= dungeon[i][n - 1];

            for (int j = n - 2; j >= 0; j--)
            {
                dp[j] = Math.max(1, Math.min(dp[j], dp[j + 1]) - dungeon[i][j]);
            }
        }

        return dp[0];
    }
}

