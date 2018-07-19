public class Solution
{
    public int maxProduct(int[] A)
    {
        if (A.length == 0)
        {
            return 0;
        }

        int maxhere, minhere;
        int maxpre = A[0];
        int minpre = A[0];
        int maxNow = A[0];

        for (int i = 1; i < A.length; i++)
        {
            maxhere = Math.max(Math.max(maxpre * A[i], minpre * A[i]), A[i]);
            minhere = Math.min(Math.min(maxpre * A[i], minpre * A[i]), A[i]);
            maxNow = Math.max(maxNow, maxhere);
            maxpre = maxhere;
            minpre = minhere;
        }

        return maxNow;
    }
}
