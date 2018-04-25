public class Solution
{
    public int minSubArrayLen(int s, int[] nums)
    {
        if (nums.length == 0 || nums == null)
        {
            return 0;
        }

        int left = 0, right = -1, sum = 0;
        int min = Integer.MAX_VALUE;

        while (right < nums.length)
        {
            while (sum < s && right < nums.length - 1)
            {
                sum += nums[++right];
                System.out.println(right);
                System.out.println(sum);
            }

            while (sum >= s)
            {
                min = Math.min(min, right - left + 1);
                sum -= nums[left++];
            }
            
            System.out.println(min);
            System.out.println();
        }

        return min == Integer.MAX_VALUE ? 0 : min;
    }
}
