public class Solution
{
    public int maximalSquare(char[][] matrix)
    {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0)
        {
            return 0;
        }

        int maxLen = 0;
        int dp[] = new int[matrix[0].length];
        Arrays.fill(dp, 0);

        for (int i = 0; i < matrix.length; i++)
        {
            for (int j = 1; j < matrix[0].length; j++)
            {
                dp[j] = matrix[i][j] == '1' ? Math .min(Math.min(dp[j], dp[j - 1]), Character.getNumericValue(matrix[i][j - 1])) + 1 : 0;
                maxLen = Math.max(maxLen, dp[j]);
            }

            dp[0] = Character.getNumericValue(matrix[i][0]);
            maxLen = Math.max(maxLen, dp[0]);
        }

        return maxLen * maxLen;
    }
}
