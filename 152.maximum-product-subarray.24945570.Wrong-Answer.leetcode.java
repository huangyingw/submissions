public class Solution
{
    public int maxProduct(int[] A)
    {
        int local = A[0];
        int global = A[0];

        for (int i = 1; i < A.length; i++)
        {
            local = Math.max(local * A[i], A[i]);
            global = Math.max(local, global);
        }

        return global;
    }
}
