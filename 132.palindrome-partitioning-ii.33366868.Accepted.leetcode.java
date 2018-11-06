  public class Solution
  {
    public int minCut(String s)
    {
      boolean dp[][] = new boolean[s.length()][s.length()];
      int cut[] = new int[s.length()];

      for (int j = 0; j < s.length(); j++)
      {
        cut[j] = j; //set maximum # of cut

        for (int i = 0; i <= j; i++)
        {
          if (s.charAt(i) == s.charAt(j) && (j - i <= 1 || dp[i + 1][j - 1]))
          {
            dp[i][j] = true;

            if (i > 0)
            {
              cut[j] = Math.min(cut[j], cut[i - 1] + 1);
            }
            else
            {
              cut[j] = 0;
            }
          }
        }
      }

      return cut[s.length() - 1];
    }
  }
