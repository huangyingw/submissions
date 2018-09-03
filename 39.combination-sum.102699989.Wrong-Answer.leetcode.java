public class Solution
{
    public List<List<Integer>> combinationSum(int[] datas, int target)
    {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        dfs(datas, 0, result, new ArrayList<Integer>(), target);
        return result;
    }

    public void dfs(int[] datas, int start, List<List<Integer>> result, List<Integer> current, int target)
    {
        if (target == 0)
        {
            result.add(new ArrayList<Integer>(current));
            return;
        }

        for (int i = start; i < datas.length; i++)
        {
            if (target < datas[i])
            {
                return;
            }

            current.add(datas[i]);
            dfs(datas, i, result, current, target - datas[i]);
            current.remove(current.size() - 1);
        }
    }
}
