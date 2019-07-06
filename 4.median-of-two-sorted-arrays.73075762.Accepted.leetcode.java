public class Solution
{
    public double findMedianSortedArrays(int A[], int B[])
    {
        int len = A.length + B.length;

        if (len % 2 == 1)
        {
            return findKth(A, 0, B, 0, len / 2 + 1);
        }

        return (
                   findKth(A, 0, B, 0, len / 2) + findKth(A, 0, B, 0, len / 2 + 1)
               ) / 2.0;
    }
    public int findKth(int[] A, int aStart, int[] B, int bStart, int k)
    {
        if (aStart >= A.length)
        {
            return B[bStart + k - 1];
        }

        if (bStart >= B.length)
        {
            return A[aStart + k - 1];
        }

        if (k == 1)
        {
            return Math.min(A[aStart], B[bStart]);
        }

        int A_key = aStart + k / 2 - 1 < A.length
                    ? A[aStart + k / 2 - 1]
                    : Integer.MAX_VALUE;
        int B_key = bStart + k / 2 - 1 < B.length
                    ? B[bStart + k / 2 - 1]
                    : Integer.MAX_VALUE;

        if (A_key < B_key)
        {
            return findKth(A, aStart + k / 2, B, bStart, k - k / 2);
        }
        else
        {
            return findKth(A, aStart, B, bStart + k / 2, k - k / 2);
        }
    }
}
