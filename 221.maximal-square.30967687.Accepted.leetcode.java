public class Solution
{
    public int maximalSquare(char[][] matrix)
    {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0)
        {
            return 0;
        }

        int maxLen = 0;
        int dp[][] = new int[matrix.length][matrix[0].length];

        for (int i = 0; i < matrix.length; i++)
        {
            dp[i][0] = Character.getNumericValue(matrix[i][0]);
            maxLen = Math.max(maxLen, dp[i][0]);
        }

        for (int j = 0; j < matrix[0].length; j++)
        {
            dp[0][j] = Character.getNumericValue(matrix[0][j]);
            maxLen = Math.max(maxLen, dp[0][j]);
        }

        for (int i = 1; i < matrix.length; i++)
        {
            for (int j = 1; j < matrix[0].length; j++)
            {
                dp[i][j] =
                    matrix[i][j] == '1' ? Math.min(Math.min(dp[i - 1][j],
                                                   dp[i][j - 1]),
                                                   dp[i - 1][j - 1]) + 1 : 0;
                maxLen = Math.max(maxLen, dp[i][j]);
            }
        }

        return maxLen * maxLen;
    }
}
