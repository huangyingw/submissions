public class Solution
{
    public int[] productExceptSelf(int[] nums)
    {
        if (nums == null)
        {
            return null;
        }

        int[] result = new int[nums.length];
        result[0] = 1;

        for (int i = 1; i < nums.length; i++)
        {
            result[i] = result[i - 1] * nums[i - 1];
        }

        int prod = 1;

        for (int i = nums.length - 2; i >= 0; i--)
        {
            prod *= nums[i + 1];
            result[i] *= prod;
        }

        return result;
    }
}
