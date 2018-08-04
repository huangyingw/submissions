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

    private void dfs(int[] num, int start, int target, ArrayList<Integer> current, ArrayList<ArrayList<Integer>> result)
    {
        if (target < 0 || start >= num.length)
        {
            return;
        }

        if (target == 0)
        {
            result.add(new ArrayList<Integer>(current));
            return;
        }

        for (int index = start; index < num.length; index++)
        {
            if (index > start && num[index] == num[index - 1])
            {
                continue;
            }

            current.add(num[index]);
            dfs(num, index + 1, target - num[index], current, result);
            current.remove(current.size() - 1);
        }
    }
}
