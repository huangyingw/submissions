public class Solution
{
    public int[] searchRange(int[] nums, int target)
    {
        int[] result = {-1, -1};

        if (nums == null || nums.length == 0)
        {
            return result;
        }

        int left = 0, right = nums.length - 1;

        while (left + 1 < right)
        {
            int mid = (left + right) / 2;

            if (nums[mid] >= target)
            {
                right = mid;
            }
            else
            {
                left = mid;
            }
        }

        if (nums[left] == target)
        {
            result[0] = left;
        }
        else if (nums[right] == target)
        {
            result[0] = right;
        }
        else
        {
            return result;
        }

        left = 0;
        right = nums.length - 1;

        while (left + 1 < right)
        {
            int mid = left + (right - left) / 2;

            if (nums[mid] <= target)
            {
                left = mid;
            }
            else
            {
                right = mid;
            }
        }

        if (nums[right] == target)
        {
            result[1] = right;
        }
        else if (nums[left] == target)
        {
            result[1] = left;
        }
        else
        {
            result[0] = result[1] = -1;
            return result;
        }

        return result;
    }
}

