public class Solution
{
    public List<List<Integer>> combinationSum3(int k, int n)
    {
        List<List<Integer>> re = new ArrayList<List<Integer>>();
        dfs(re, 1, 0, k, n, new ArrayList<Integer>());
        return re;
    }

    private void dfs(List<List<Integer>> result, int start, int target, int k,
                     int n, List<Integer> current)
    {
        if (target > n || current.size() > k)
        {
            return;
        }

        if (current.size() == k && target == n)
        {
            result.add(new ArrayList<Integer>(current));
            return;
        }

        for (int index = start; index <= 9; index++)
        {
            current.add(index);
            dfs(result, index + 1, target + index, k, n, current);
            current.remove(current.size() - 1);
        }
    }
}
