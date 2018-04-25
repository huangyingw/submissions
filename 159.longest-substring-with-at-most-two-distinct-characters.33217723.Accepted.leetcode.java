  public class Solution
  {
    public int lengthOfLongestSubstringTwoDistinct(String s)
    {
      int start = 0, end = -1, maxLen = 0;

      for (int k = 1; k < s.length(); k++ )
      {
        if (s.charAt(k) == s.charAt(k - 1))
        {
          continue;
        }

        if (end >= 0 && s.charAt(end) != s.charAt(k))
        {
          maxLen = Math.max(k - start, maxLen);
          start = end + 1;
        }

        end = k - 1;
      }

      return Math.max(s.length() - start, maxLen);
    }
  }

