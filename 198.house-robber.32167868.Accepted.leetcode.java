  public class Solution
  {
    public int rob(int[] num)
    {
      int a = 0, b = 0;

      for (int i = 0; i < num.length; i++)
      {
        int m = a, n = b;
        a = n + num[i];
        b = Math.max(m, n);
      }

      return Math.max(a, b);
    }
  }

