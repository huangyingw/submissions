public class Solution
{
    public int[] twoSum(final int[] nums, int target)
    {
        int[] result = new int[2];
        Arrays.sort(nums);
        int left = 0;
        int right = nums.length - 1;

        while (left < right)
        {
            if ((nums[left] + nums[right]) > target)
            {
                right--;
            }
            else if ((nums[left] + nums[right]) < target)
            {
                left++;
            }
            else
            {
                result[0] = left;
                result[1] = right;
            }
        }

        return result;
    }
}
