public class Solution
{
    public List<List<Integer>> permute(int[] num)
    {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        dfs(num, 0, new ArrayList<Integer>(), result);
        return result;
    }

    public void dfs(int[] num, int start, List<Integer> current, List<List<Integer>> result)
    {
        if (current.size() == num.length)
        {
            result.add(new ArrayList<Integer>(current));
            return;
        }

        for (int idx = start; idx < num.length; idx++)
        {
            current.add(num[idx]);
            dfs(num, idx + 1, current, result);
            current.remove(current.size() - 1);
        }
    }
}
