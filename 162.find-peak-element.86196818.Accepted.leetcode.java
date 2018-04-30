class Solution
{
    /**
        * @param A: An integers array.
        * @return: return any of peek positions.
        */
    public int findPeakElement(int[] A)
    {
        if (A.length == 1)
        {
            return 0;
        }

        // write your code here
        int start = 0, end = A.length - 1; // 1.答案在之间，2.不会出界

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

