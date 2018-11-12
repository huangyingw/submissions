public class Solution
{
    public int threeSumSmaller(int[] nums, int target)
    {
        Arrays.sort(nums);
        int cnt = 0;

        for (int i = 0; i < nums.length - 2; i++)
        {
            int left = i + 1, right = nums.length - 1;

            while (left < right)
            {
                if (nums[i] + nums[left] + nums[right] < target)
                {
                    cnt += right - left;
                    continue;
                }
                else
                {
                    right++;
                }
            }
        }

        return cnt;
    }
}
