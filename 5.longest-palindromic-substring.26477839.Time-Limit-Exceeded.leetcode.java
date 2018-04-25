public class Solution
{
    public String longestPalindrome(String s)
    {
        int len = s.length();

        if (len <= 1)
        {
            return s;
        }

        int maxLen = 1;

        for (int i = 1; i < len;)
        {
            int low = i - 1, high = i;

            while (low >= 0 && high < len && s.charAt(low) == s.charAt(high))
            {
                low--;
                high++;
            }

            if (high - low - 1 > maxLen)
            {
                maxLen = high - low - 1;
            }

            low = i - 1;
            high = i + 1;

            while (low >= 0 && high < len && s.charAt(low) == s.charAt(high))
            {
                low--;
                high++;
            }

            if (high - low - 1 > maxLen)
            {
                maxLen = high - low - 1;
            }
        }

        return s.substring(0, maxLen);
    }
}

