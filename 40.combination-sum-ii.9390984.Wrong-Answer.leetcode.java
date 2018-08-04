public class Solution
{
    public ArrayList<ArrayList<Integer>> combinationSum2(int[] nums, int target)
    {
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();

        if (nums == null || nums.length == 0)
        {
            return result;
        }

        Arrays.sort(nums);
        dfs(nums, 0, target, new ArrayList<Integer>(), result);
        return result;
    }

    private void dfs(int[] nums, int start, int target, ArrayList<Integer> current, ArrayList<ArrayList<Integer>> result)
    {
        if (target < 0 || start >= nums.length)
        {
            return;
        }

        if (target == 0)
        {
            result.add(new ArrayList<Integer>(current));
            return;
        }

        for (int index = start; index < nums.length; index++)
        {
            if (index > start && nums[index] == nums[index - 1])
            {
                continue;
            }

            current.add(nums[index]);
            dfs(nums, index + 1, target - nums[index], current, result);
            current.remove(current.size() - 1);
        }
    }
}
