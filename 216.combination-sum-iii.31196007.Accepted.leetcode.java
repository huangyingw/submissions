public class Solution
{
    public List<List<Integer>> combinationSum3(int k, int n)
    {
        List<List<Integer>> re = new ArrayList<List<Integer>>();
        dfs(re, 1, 0, k, n, new ArrayList<Integer>());
        return re;
    }

    private void dfs(List<List<Integer>> result, int index, int sum, int k, int n,
                     List<Integer> current)
    {
        if (sum > n || current.size() > k)
        {
            return;
        }

        if (current.size() == k && sum == n)
        {
            result.add(new ArrayList<Integer>(current));
        }
        else
        {
            for (int i = index; i <= 9; i++)
            {
                current.add(i);
                dfs(result, i + 1, sum + i, k, n, current);
                current.remove(current.size() - 1);
            }
        }
    }
}
