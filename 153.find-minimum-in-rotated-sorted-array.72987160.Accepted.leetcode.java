public class Solution
{
    public int findMin(int[] nums)
    {
        if (nums == null || nums.length == 0)
        {
            return 0;
        }

        int left = 0;
        int right = nums.length - 1;

        while (left + 1 < right)
        {
            if (nums[left] < nums[right])
            {
                return nums[left];
            }

            int mid = left + (right - left) / 2;

            if (nums[mid] < nums[left])
            {
                right = mid;
            }
            else
            {
                left = mid;
            }
        }

        return Math.min(nums[left], nums[right]);
    }
}

