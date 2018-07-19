public class Solution
{
    public int firstMissingPositive(int[] A)
    {
        for (int i = 0; i < A.length; i++)
        {
            // if it's not in its supposed to be place (the index of value x should
            // be x - 1)
            if (i != A[i] - 1)
            {
                if (A[i] <= 0 || A[i] > A.length || A[i] == A[A[i] - 1])
                {
                    continue;
                }
                else
                {
                    // put A[i] to A[A[i] - 1]
                    int temp = A[i];
                    A[i] = A[A[i] - 1];
                    A[A[i] - 1] = temp;
                    // i--;
                }
            }
        }

        for (int i = 0; i < A.length; i++)
        {
            if (i != A[i] - 1)
            {
                return i + 1;
            }
        }

        return A.length + 1;
    }
}
