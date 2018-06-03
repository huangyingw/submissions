public class Solution
{
    public List<List<String>> solveNQueens(int n)
    {
        List<List<String>> res = new ArrayList<List<String>>();
        solveNQ(n, 0, new int[n], res);
        return res;
    }

    private void solveNQ(int n, int row, int[] queens, List<List<String>> res)
    {
        if (row == n)
        {
            List<String> strs = new ArrayList<String>();
            char[] arr = new char[n];
            Arrays.fill(arr, '.');

            for (int i = 0; i < n; i++)
            {
                arr[queens[i]] = 'Q';
                strs.add(new String(arr));
                arr[queens[i]] = '.';
            }

            res.add(strs);
            return;
        }

        for (int col = 0; col < n; col++)
        {
            if (fit(n, queens, row, col))
            {
                queens[row] = col;
                solveNQ(n, row + 1, queens, res);
            }
        }
    }

    private boolean fit(int n, int[] queens, int row, int col)
    {
        int leftTop = col;
        int rightTop = col;

        for (int i = row - 1; i >= 0; i--)
        {
            leftTop--;
            rightTop++;

            if (queens[i] == col || queens[i] == leftTop || queens[i] == rightTop)
            {
                return false;
            }
        }

        return true;
    }
}

