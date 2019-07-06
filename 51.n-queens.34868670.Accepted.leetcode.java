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
            char[] strRow = new char[n];
            Arrays.fill(strRow, '.');

            for (int row = 0; row < n; row++)
            {
                strRow[columnForRow[row]] = 'Q';
                board.add(new String(strRow));
                strRow[columnForRow[row]] = '.';
            }

            result.add(board);
            return;
        }

        for (int col = 0; col < n; col++)
        {
            if (isValid(columnForRow, curRow, col))
            {
                columnForRow[curRow] = col;
                dfs(result, columnForRow, curRow + 1, n);
            }
        }
    }
    public boolean isValid(int[] columnForRow, int curRow, int col)
    {
        int leftTop = col;
        int rightTop = col;

        for (int row = curRow - 1; row >= 0; row--)
        {
            leftTop--;
            rightTop++;

            if (columnForRow[row] == col || columnForRow[row] == leftTop || columnForRow[row] == rightTop)
            {
                return false;
            }
        }

        return true;
    }
}
