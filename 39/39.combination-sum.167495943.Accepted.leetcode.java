public class Solution
{
    public List<List<Integer>> combinationSum(int[] nums, int target)
    {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        helper(nums, 0, result, new ArrayList<Integer>(), target);
        return result;
    }

    public void helper(int[] nums, int start, List<List<Integer>> result, List<Integer> current, int target)
    {
        if (target == 0)
        {
            result.add(new ArrayList<Integer>(current));
        }

        for (int i = start; i < nums.length; i++)
        {
            if (target < nums[i])
            {
                return;
            }

            current.add(nums[i]);
            System.out.printf("current --> %s\n", current);
            helper(nums, i, result, current, target - nums[i]);
            current.remove(current.size() - 1);
        }
    }
}

