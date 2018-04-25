  public class Solution
  {
    private void rev(int [] num, int beg, int end)
    {
      while (beg < end)
      {
        int tmp = num[beg];
        num[beg] = num[end];
        num[end] = tmp;
        beg ++;
        end --;
      }
    }
    public void rotate(int[] nums, int k)
    {
      k = k % nums.length;

      if (k <= 0)
      {
        return;
      }

      rev(nums, 0, nums.length - 1);
      rev(nums, 0, k - 1);
      rev(nums, k, nums.length - 1);
    }
  }

