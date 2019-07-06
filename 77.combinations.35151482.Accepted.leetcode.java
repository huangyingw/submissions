public class Solution
{
    private void dfs(int start, int end, int k, List<Integer> current,
                     List<List<Integer>> result)
    {
        if (k == 0)
        {
            result.add(new ArrayList<Integer>(current));
            return;
        }

        for (int index = start; index <= end - k + 1; index++)
        {
            current.add(index);
            dfs(index + 1, end, k - 1, current, result);
            current.remove(current.size() - 1);
        }
    }
    public List<List<Integer>> combine(int n, int k)
    {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        dfs(1, n, k, new ArrayList<Integer>(), result);
        return result;
    }
}
