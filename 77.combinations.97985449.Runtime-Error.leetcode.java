public class Solution
{
    public List<List<Integer>> combine(int n, int k)
    {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        List<Integer> cur = new ArrayList<Integer>();
        dfs(1, n, k, result, cur);
        return result;
    }
    public void dfs(int l, int r, int k, List<List<Integer>> res, List<Integer> cur)
    {
        if (k == 0)
        {
            res.add(new ArrayList<Integer>(cur));
        }

        for (int i = l; i <= r - k + 1; i++)
        {
            cur.add(i);
            dfs(i + 1, r, k - 1, res, cur);
            cur.remove(cur.size() - 1);
        }
    }
}