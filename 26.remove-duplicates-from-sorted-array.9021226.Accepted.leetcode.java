public class Solution
{
    public int removeDuplicates(int[] A)
    {
        assert A != null;

        if (A.length == 0)
        {
            return 0;
        }

        int distinctCount = 1;

        for (int i = 1; i < A.length; i++)
        {
            if (A[distinctCount - 1] != A[i])
            {
                A[distinctCount++] = A[i];
            }
        }

        return distinctCount;
    }
}
