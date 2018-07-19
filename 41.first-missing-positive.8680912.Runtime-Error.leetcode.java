public class Solution
{
    public int firstMissingPositive(int[] A)
    {
        int n = A.length;
        int i = 0;

        while (i < n)
        {
            if (A[i] >= 0 && A[i] < n && A[A[i]] != A[i])
            {
                A[i] ^= A[A[i]];
                A[A[i]] ^= A[i];
                A[i] ^= A[A[i]];
            }
            else
            {
                i++;
            }
        }

        int k = 1;

        while (k < n && A[k] == k)
        {
            k++;
        }

        if (n == 0 || k < n)
        {
            return k;
        }
        else
        {
            return A[0] == k ? k + 1 : k;
        }
    }
}
