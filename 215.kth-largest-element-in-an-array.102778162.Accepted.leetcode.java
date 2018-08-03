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
            }
            else if (data[left] >= pivot)
            {
                left++;
            }
            else
            {
                int temp = data[left];
                data[left] = data[right];
                data[right] = temp;
            }
        }

        data[l] = data[right];
        data[right] = pivot;
        return right;
    }

    private int select(int[] nums, int k, int left, int right)
    {
        while (left < right)
        {
            int pivot = partition(nums, left, right);

            if (pivot + 1 == k)
            {
                return nums[pivot];
            }
            else if (pivot + 1 > k)
            {
                right = pivot - 1;
            }
            else
            {
                left = pivot + 1;
            }
        }

        return nums[left];
    }
}
