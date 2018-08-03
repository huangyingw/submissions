public class Solution
{
    public int[] searchRange(int[] nums, int target)
    {
        int[] result = { -1, -1 };

        if (nums == null || nums.length == 0)
        {
            return result;
        }

        int left = 0, right = nums.length - 1;

        while (left < right)
        {
            int mid = left + (right - left) / 2;

            if (nums[mid] >= target)
            {
                right = mid;
            }
            else
            {
                left = mid + 1;
            }
        }

        if (nums[left] == target)
        {
            result[0] = left;
        }
        else
        {
            return result;
        }

        left = 0;
        right = nums.length - 1;

        while (left < right)
        {
            int mid = left + (right - left) / 2;

            if (nums[mid] <= target)
            {
                left = mid + 1;
            }
            else
            {
                right = mid;
            }
        }

        if (left == 0)
        {
            if (nums[left] == target)
            {
                result[1] = left;
            }
        }
        else if (nums[left - 1] == target)
        {
            result[1] = left - 1;
        }
        else
        {
            result[0] = result[1] = -1;
            return result;
        }

        return result;
    }
}
