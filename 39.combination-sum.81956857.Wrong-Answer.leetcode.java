public class Solution
{
    public List<List<Integer>> combinationSum(int[] candidates, int target)
    {
        Arrays.sort(candidates);
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        dfs(candidates, 0, result, new ArrayList<Integer>(), target);
        return result;
    }
    public void dfs(int[] candidates, int start, List<List<Integer>> result, List<Integer> current, int target)
    {
        if (target == 0)
        {
            result.add(current);
        }

        for (int i = start; i < candidates.length; i++)
        {
            if (candidates[i] > target)
            {
                return;
            }

            current.add(candidates[i]);
            dfs(candidates, i, result, current, target - candidates[i]);
            current.remove(current.size() - 1);
        }
    }
}
