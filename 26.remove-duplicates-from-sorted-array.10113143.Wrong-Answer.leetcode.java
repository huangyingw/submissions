public class Solution
{
    public int removeDuplicates(int[] A)
    {
        if (A.length < 2)
        {
            return A.length;
        }

        int index = 0;

        for (int i = 1; i < A.length; i++)
        {
            if (A[index] != A[i])
            {
                A[++index] = A[i];
            }
        }

        return index;
    }
}
