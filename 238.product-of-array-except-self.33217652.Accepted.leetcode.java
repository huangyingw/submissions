public class Solution
{
    public int[] productExceptSelf(int[] nums)
    {
        if (nums == null)
        {
            return null;
        }

        int[] result = new int[nums.length];

        for (int i = 0; i < nums.length; i++)
        {
            if (i == 0)
            {
                result[i] = 1;
            }
            else
            {
                result[i] = result[i - 1] * nums[i - 1];
            }
        }

        int prod = 1;

        for (int i = nums.length - 1; i >= 0; i--)
        {
            result[i] = result[i] * prod;
            prod *= nums[i];
        }

        return result;
    }
}
