class Solution
{
    public int findPeakElement(int[] A)
    {
        if (A.length == 1)
        {
            return A[0];
        }

        int start = 1, end = A.length - 2;

        while (start + 1 <  end)
        {
            int mid = (start + end) / 2;

            if (A[mid] < A[mid - 1])
            {
                end = mid;
            }
            else if (A[mid] < A[mid + 1])
            {
                start = mid;
            }
            else
            {
                end = mid;
            }
        }

        if (A[start] < A[end])
        {
            return end;
        }
        else
        {
            return start;
        }
    }
}
