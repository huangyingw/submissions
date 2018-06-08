public class Solution
{
    public List<List<String>> solveNQueens(int n)
    {
        List<List<String>> result = new ArrayList<List<String>>();
        dfs(result, new int[n], 0, n);
        return result;
    }

    public void dfs(List<List<String>> result, int[] usedColumns, int curRow, int n)
    {
        if (curRow == n)
        {
            List<String> board = new ArrayList<String>();

            for (int row = 0; row < n; row++)
            {
                StringBuilder sb = new StringBuilder();

                for (int col = 0; col < n; col++)
                {
                    if (col == usedColumns[row])
                    {
                        sb.append("Q");
                    }
                    else
                    {
                        sb.append(".");
                    }
                }

                board.add(sb.toString());
            }

            result.add(board);
            return;
        }

        for (int col = 0; col < n; col++)
        {
            usedColumns[curRow] = col;

            if (isValidSolution(curRow, usedColumns))
            {
                dfs(result, usedColumns, curRow + 1, n);
            }

            usedColumns[curRow] = -1;
        }
    }

    private boolean isValidSolution(int curRow, int[] usedColumns)
    {
        for (int row = 0; row < curRow; row++)
        {
            if (usedColumns[row] == usedColumns[curRow]
                    || curRow - row == Math.abs(usedColumns[row] - usedColumns[curRow]))
            {
                return false;
            }
        }

        return true;
    }
}
