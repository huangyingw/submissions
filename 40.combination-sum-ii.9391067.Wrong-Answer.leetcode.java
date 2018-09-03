public class Solution
{

    public ArrayList<ArrayList<Integer>> combinationSum2(int[] num,
            int target)
    {
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();

        if (num == null || num.length == 0)
        {
            return result;
        }

        Arrays.sort(num);
        dfs(num, 0, target, new ArrayList<Integer>(), result);
        return result;
    }

    private void dfs(int[] num, int start, int target,
                     ArrayList<Integer> item,
                     ArrayList<ArrayList<Integer>> result)
    {
        if (target < 0 || start >= num.length)
        {
            return;
        }

        if (target == 0)
        {
            result.add(new ArrayList<Integer>(item));
            return;
        }

        for (int i = start; i < num.length; i++)
        {
            if (i > start && num[i] == num[i - 1])
            {
                continue;
            }

            item.add(num[i]);
            dfs(num, i + 1, target - num[i], item, result);
            item.remove(item.size() - 1);
        }
    }
}
