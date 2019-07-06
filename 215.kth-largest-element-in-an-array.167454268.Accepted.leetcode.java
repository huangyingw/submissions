public class Solution
{
    public int findKthLargest(int[] nums, int k)
    {
        return select(nums, k, 0, nums.length - 1);
    }
    int partition(int[] data, int left, int right)
    {
        int pivot = data[left];
        int i = left + 1;
        int j = right;

        while (i <= j)
        {
            if (data[i] >= pivot)
            {
                i++;
            }
            else if (data[j] < pivot)
            {
                j--;
            }
            else
            {
                int tmp = data[i];
                data[i] = data[j];
                data[j] = tmp;
                i++;
                j--;
            }
        }

        data[left] = data[j];
        data[j] = pivot;
        return j;
    }
    private int select(int[] nums, int k, int left, int right)
    {
        int pivot = 0;

        while (left <= right)
        {
            pivot = partition(nums, left, right);

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

        return nums[pivot];
    }
}
