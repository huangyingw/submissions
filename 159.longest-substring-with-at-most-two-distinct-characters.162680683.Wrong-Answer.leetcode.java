public class Solution
{
    public int lengthOfLongestSubstringTwoDistinct(String s)
    {
        int left = 0, j = -1, maxLen = 0;

        for (int right = 1; right < s.length(); right++)
        {
            if (j >= 0 && s.charAt(j) != s.charAt(right))
            {
                maxLen = Math.max(right - left, maxLen);
                left = j + 1;
            }

            j = right - 1;
        }

        return Math.max(s.length() - left, maxLen);
    }
}

