class Solution
{
    /**
     * Get all distinct N-Queen solutions
     * @param n: The number of queens
     * @return: All distinct solutions
     * For example, A string '...Q' shows a queen on forth position
     */
    List<List<String>> solveNQueens(int n)
    {
        // write your code here
        List<List<String>> resultList = new ArrayList<>();

        if (n <= 0)
        {
            return resultList;
        }

        int[] row = new int[n];
        solveNQueensCore(resultList, row, n, 0);
        return resultList;
    }

    private void solveNQueensCore(List<List<String>> resultList,
                                  int[] row,
                                  int n,
                                  int index)
    {
        if (index == n)
        {
            ArrayList<String> singleResult = translateString(row);
            resultList.add(singleResult);
            return;
        }

        for (int i = 0; i < n; i++)
        {
            if (isValid(row, index, i))
            {
                row[index] = i;
                solveNQueensCore(resultList, row, n, index + 1);
                row[index] = 0;
            }
        }
    }

    private ArrayList<String> translateString(int[] row)
    {
        ArrayList<String> resultList = new ArrayList<>();

        for (int i = 0; i < row.length; i++)
        {
            StringBuilder sb = new StringBuilder();

            for (int j = 0; j < row.length; j++)
            {
                if (j == row[i])
                {
                    sb.append('Q');
                }
                else
                {
                    sb.append('.');
                }
            }

            resultList.add(sb.toString());
        }

        return resultList;
    }

    private boolean isValid(int[] row, int rowNum, int columnNum)
    {
        for (int i = 0; i < rowNum; i++)
        {
            if (row[i] == columnNum)
            {
                return false;
            }

            if (Math.abs(row[i] - columnNum) == Math.abs(i - rowNum))
            {
                return false;
            }
        }

        return true;
    }

}
