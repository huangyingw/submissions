public class Solution
{
    public int findMin(int[] num)
    {
        if (num == null || num.length == 0)
        {
            return 0;
        }

        int start = 0;
        int end = num.length - 1;

        if ((end - start) <= 1)
        {
            return Math.min(num[start], num[end]);
        }

        while (start < end - 1)
        {
            int mid = start + (end - start) / 2;

            if (num[start] < num[end])
            {
                return num[start];
            }

            if (num[mid] > num[start])
            {
                start = mid;
            }
            else if (num[mid] < num[start])
            {
                end = mid;
            }
            else
            {
                start++;
            }
        }

        return Math.min(num[start], num[end]);
    }
}

