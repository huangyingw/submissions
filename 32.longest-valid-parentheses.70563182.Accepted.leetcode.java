public class Solution
{
    public int longestValidParentheses(String s)
    {
        if (s == null || s.length() == 0)
        {
            return 0;
        }

        // in this case, result[i] means the max length of parensis ended at i; if not, then result[i] = 0
        int[] result = new int[s.length()];
        int open = 0, max = 0;

        for (int i = 0; i < s.length(); i++)
        {
            char c = s.charAt(i);

            if (c == '(')
            {
                open++;
                //result[i] = result[i-1];
            }
            else
            {
                if (open > 0)
                {
                    result[i] = result[i - 1] + 2;

                    // important lines here
                    if (i >= result[i])
                    {
                        result[i] += result[i - result[i]];
                    }

                    open--;
                }
            }

            max = Math.max(max, result[i]);
        }

        return max;
    }
}
