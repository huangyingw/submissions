  public class Solution
  {
    public int findMin(int[] num)
    {
      int start = 0, end = num.length - 1;

      while (start < end)
      {
        int mid = start + (end - start) / 2;

        if (num[mid] < num[end])
        {
          end = mid;
        }
        else
        {
          start = mid + 1;
        }
      }

      return num[start];
    }
  }

