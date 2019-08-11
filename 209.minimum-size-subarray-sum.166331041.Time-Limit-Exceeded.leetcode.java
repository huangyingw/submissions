public class Solution
{
    public int minSubArrayLen(int s, int[] nums)
    {
        int left = 0, right = 0, sum = 0;
        int min = Integer.MAX_VALUE;

        while (right < nums.length)
        {
            if (sum < s)
            {
                sum += nums[right];

                if (right + 1 < nums.length)
                {
                    right++;
                }
            }
            else
            {
                min = Math.min(min, right - left);
                sum -= nums[left];

                if (left + 1 < nums.length)
                {
                    left++;
                }
            }
        }

        return min == Integer.MAX_VALUE ? 0 : min;
    }
}
