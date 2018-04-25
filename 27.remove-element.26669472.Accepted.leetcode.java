public class Solution
{
    public int removeElement(int[] A, int elem)
    {
        int index = 0;

        for (int nav = 0; nav < A.length; nav++)
        {
            if (A[nav] != elem)
            {
                A[index++] = A[nav];
            }
        }

        return index;
    }
}
