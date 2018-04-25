public class Solution
{
    public boolean canJump(int[] A)
    {
        int maxD = 0;
        int index = 0;

        while (index <= maxD)
        {
            if (maxD >= A.length - 1)
            {
                return true;
            }

            maxD = Math.max(maxD, index + A[index++]);
        }

        return false;
    }
}
