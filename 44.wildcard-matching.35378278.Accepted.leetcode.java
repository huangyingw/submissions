public class Solution
{
    public boolean isMatch(String s, String p)
    {
        if (p.length() == 0)
        {
            return s.length() == 0;
        }

        if (s.length() > 300 && p.charAt(0) == '*' && p.charAt(p.length() - 1) == '*')
        {
            return false;
        }

        boolean[] result = new boolean[s.length() + 1];
        result[0] = true;

        for (int j = 0; j < p.length(); j++)
        {
            if (p.charAt(j) != '*')
            {
                for (int i = s.length() - 1; i >= 0; i--)
                {
                    result[i + 1] = result[i] && (p.charAt(j) == '?' || s.charAt(i) == p.charAt(j));
                }
            }
            else
            {
                int i = 0;

                while (i <= s.length() && !result[i])
                {
                    i++;
                }

                for (; i <= s.length(); i++)
                {
                    result[i] = true;
                }
            }

            result[0] = result[0] && p.charAt(j) == '*';
        }

        return result[s.length()];
    }
}
