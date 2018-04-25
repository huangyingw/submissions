  public class Solution
  {
    public int[] productExceptSelf(int[] nums)
    {
      if (nums == null)
      {
        return null;
      }

      int[] res = new int[nums.length];

      for (int i = 0; i < nums.length; i++)
      {
        if (i == 0)
        {
          res[i] = 1;
        }
        else
        {
          res[i] = res[i - 1] * nums[i - 1];
        }
      }

      int prod = 1;

      for (int i = nums.length - 1; i >= 0; i--)
      {
        res[i] = res[i] * prod;
        prod *= nums[i];
      }

      return res;
    }
  }

