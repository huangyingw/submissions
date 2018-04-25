public class Solution
{
    public String countAndSay(int n)
    {
        String str = "1";

        for (int i = 0; i < n; i++)
        {
            int count = 1;
            StringBuilder sb = new StringBuilder();

            for (int nav = 0; nav < str.length(); nav++)
            {
                if (nav + 1 < str.length() && str.charAt(nav) == str.charAt(nav + 1))
                {
                    count++;
                }
                else
                {
                    sb.append("" + count).append(str.charAt(nav));
                    count = 0;

                    if (nav == str.length() - 2)
                    {
                        sb.append("1").append(str.charAt(str.length() - 1));
                    }
                }
            }

            str = sb.toString();
        }

        return str;
    }
}
