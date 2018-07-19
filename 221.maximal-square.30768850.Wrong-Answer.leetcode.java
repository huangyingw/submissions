public class Solution
{
    public int maximalSquare(char[][] matrix)
    {
        char[][] m = matrix;

        if (m.length == 0 || m[0].length == 0)
        {
            return 0;
        }

        int max = 0;
        int[] res = new int[m[0].length];

        for (int i = 0; i < m[0].length; i++)
        {
            res[i] = m[0][i] - '0';
            max = Math.max(res[i], max);
        }

        for (int i = 1; i < m.length; i++)
        {
            int[] newRes = new int[m[0].length];
            newRes[0] = m[i][0] - '0';
            max = Math.max(newRes[0], max);

            for (int j = 1; j < m[0].length; j++)
            {
                if (m[i][j] == '1')
                {
                    newRes[j] =
                        Math.min(Math.min(res[j - 1], res[j]), newRes[j - 1]) + 1;
                }
                else
                {
                    newRes[j] = 0;
                }

                max = Math.max(newRes[j], max);
            }

            res = newRes;
        }

        return max;
    }
}
