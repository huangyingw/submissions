public class Solution
{
    public int findPeakElement(int[] num)
    {
        int left = 0;
        int right = num.length - 1;

        while (left <= right)
        {
            int mid = left + (right - left) / 2;

            if (mid == 0 || num[mid - 1] < num[mid])
            {
                if (mid + 1 == num.length || num[mid] > num[mid + 1])
                {
                    return mid;
                }

                left = mid + 1;
            }
            else
            {
                right = mid - 1;
            }
        }

        return -1;
    }
}

