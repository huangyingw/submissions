public class Solution
{
    public int lengthOfLongestSubstringTwoDistinct(String s)
    {
        int[] count = new int[256];
        int i = 0, numDistinct = 0, maxLen = 0;

        for (int j = 0; j < s.length(); j++)
        {
            if (count[s.charAt(j)] == 0)
            {
                numDistinct++;
            }

            count[s.charAt(j)]++;
            maxLen = Math.max(j - i + 1, maxLen);
        }

        return maxLen;
    }
}
