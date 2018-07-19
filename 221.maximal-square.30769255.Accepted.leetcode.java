public class Solution
{
    public int maximalSquare(char[][] matrix)
    {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0)
        {
            return 0;
        }

        int maxLen = 0;
        int res[][] = new int[matrix.length][matrix[0].length];

        for (int i = 0; i < matrix.length; i++)
        {
            res[i][0] = Character.getNumericValue(matrix[i][0]);
            maxLen = Math.max(maxLen, res[i][0]);
        }

        for (int j = 0; j < matrix[0].length; j++)
        {
            res[0][j] = Character.getNumericValue(matrix[0][j]);
            maxLen = Math.max(maxLen, res[0][j]);
        }

        for (int i = 1; i < matrix.length; i++)
        {
            for (int j = 1; j < matrix[0].length; j++)
            {
                res[i][j] =
                    matrix[i][j] == '1' ? Math.min(Math.min(res[i - 1][j],
                                                   res[i][j - 1]),
                                                   res[i - 1][j - 1]) + 1 : 0;
                maxLen = Math.max(maxLen, res[i][j]);
            }
        }

        return maxLen * maxLen;
    }
}
