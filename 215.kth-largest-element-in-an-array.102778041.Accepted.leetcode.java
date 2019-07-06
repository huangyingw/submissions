public class Solution
{
    public int findKthLargest(int[] nums, int k)
    {
        return select(nums, k, 0, nums.length - 1);
    }
    int partition(int[] data, int l, int r)
    {
        int left = l + 1;
        int right = r;
        int pivot = data[l];

        while (left <= right)
        {
            if (data[right] < pivot)
            {
                right--;
                continue;
            }

            if (data[left] >= pivot)
            {
                left++;
                continue;
            }

            int temp = data[left];
            data[left] = data[right];
            data[right] = temp;
        }

        data[l] = data[right];
        data[right] = pivot;
        return right;
    }
    private int select(int[] nums, int k, int left, int right)
    {
        int pivot = partition(nums, left, right);

        if (pivot + 1 == k)
        {
            return nums[pivot];
        }
        else if (pivot + 1 > k)
        {
            return select(nums, k, left, pivot - 1);
        }
        else
        {
            return select(nums, k, pivot + 1, right);
        }
    }
}
