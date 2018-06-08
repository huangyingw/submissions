public class Solution
{
    public List<List<String>> solveNQueens(int n)
    {
        List<List<String>> result = new ArrayList<List<String>>();
        dfs(result, new int[n], 0, n);
        return result;
    }

    public void dfs(List<List<String>> result, int[] columnForRow, int curRow, int n)
    {
        if (curRow == n)
        {
            List<String> board = new ArrayList<String>();

            for (int row = 0; row < n; row++)
            {
                StringBuilder strRow = new StringBuilder();

                for (int col = 0; col < n; col++)
                {
                    if (col == columnForRow[row])
                    {
                        strRow.append("Q");
                    }
                    else
                    {
                        strRow.append(".");
                    }
                }

                board.add(strRow.toString());
            }

            result.add(board);
            return;
        }

        for (int col = 0; col < n; col++)
        {
            columnForRow[curRow] = col;

            if (isValid(curRow, columnForRow))
            {
                dfs(result, columnForRow, curRow + 1, n);
            }

            columnForRow[curRow] = -1;
        }
    }

    private boolean isValid(int curRow, int[] columnForRow)
    {
        for (int row = 0; row < curRow; row++)
        {
            if (columnForRow[row] == columnForRow[curRow] || curRow - row == Math.abs(columnForRow[row] - columnForRow[curRow]))
            {
                return false;
            }
        }

        return true;
    }
}
