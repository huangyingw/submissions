public class Solution
{
    public int[] singleNumber(int[] nums)
    {
        int[] result = new int[2];
        result[0] = 0;
        result[1] = 0;
        int n = 0;

        for (int elem : nums)
        {
            n ^= elem;
        }

        n = n & (~(n - 1));

        for (int elem : nums)
        {
            if ((elem & n) != 0)
            {
                result[0] ^= elem;
            }
            else
            {
                result[1] ^= elem;
            }
        }

        return result;
    }
}
