public class Solution
{
    public int lengthOfLongestSubstringTwoDistinct(String s)
    {
        int left = 0, j = -1, maxLen = 0;

        for (int right = 1; right < s.length(); right++)
        {
            if (s.charAt(right) == s.charAt(right - 1))
            {
                continue;
            }

            j = right - 1;
        }

        return Math.max(s.length() - left, maxLen);
    }
}

