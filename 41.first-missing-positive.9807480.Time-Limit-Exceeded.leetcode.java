public class Solution
{
    public int firstMissingPositive(int[] A)
    {
        int i = 0;
        int n = A.length;

        while (i < n)
        {
            if (A[i] != (i + 1) && A[i] >= 1 && A[i] <= n && A[A[i] - 1] != A[i])
            {
                int temp = A[i];
                A[i] = A[A[i] - 1];
                A[A[i] - 1] = temp;
            }
            else
            {
                i++;
            }
        }

        for (i = 0; i < n; ++i)
            if (A[i] != (i + 1))
            {
                return i + 1;
            }

        return n + 1;
    }
}

