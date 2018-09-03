public class Solution
{
    public List<List<Integer>> combine(int n, int k)
    {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        List<Integer> cur = new ArrayList<Integer>();
        dfs(1, n, k, result, cur);
        return result;
    }
    public void dfs(int l, int r, int k, List<List<Integer>> result, List<Integer> cur)
    {
        if (k == 0)
        {
            result.add(new ArrayList<Integer>(cur));
            return;
        }

        for (int i = l; i <= r - k + 1; i++)
        {
            cur.add(l);
            dfs(l + 1, r, k - 1, result, cur);
            cur.remove(cur.size() - 1);
        }
    }
}
